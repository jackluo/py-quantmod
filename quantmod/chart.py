"""Main Chart functionnality

Includes Quantmod plotting engine.

"""
from __future__ import absolute_import

import copy
import six
import numpy as np
import pandas as pd
import plotly.plotly as py
import plotly.offline as pyo

import talib  # To be removed

from . import auth
from . import utils
from . import tools
from .valid import *
from .ta import *


class Chart(object):
    """Quantmod Chart based on Pandas DataFrame.

    Features include time series adjustement, volume adjustement, and plotting.

    """

    def __init__(self, df, source=None,
                 ticker=None, start=None, end=None):
        """ADD INFO

        ADD DOCUMENTATION

        """

        """ADD ERROR HANDLING"""

        # Test if source is str or dict, or get default vendor otherwise
        if source:
            if isinstance(source, six.string_types):
                source = tools.get_source(source)
            elif isinstance(source, dict):
                pass
            else:
                raise Exception("Invalid source '{0}'.".format(source))
        else:
            source = tools.get_source(auth.get_config_file()['source'])

        """
        Ticker,
        Start,
        End
        """

        self.df = df

        self.ticker = ticker
        self.start = self.df.index[0]
        self.end = self.df.index[-1]

        self.op = source['op']
        self.hi = source['hi']
        self.lo = source['lo']
        self.cl = source['cl']
        self.aop = source['aop'] # Not used currently
        self.ahi = source['ahi'] # Not used currently
        self.alo = source['alo'] # Not used currently
        self.acl = source['acl']
        self.vo = source['vo']
        self.di = source['di'] # Not used currently

        self.ind = pd.DataFrame([], index=self.df.index)
        self.pri = {}
        self.sec = {}

    def __repr__(self):
        """Return representation of Chart object."""
        return str(self.to_frame())

    def __len__(self):
        """Return length of Chart object."""
        return len(self.to_frame())

    @property
    def shape(self):
        """Return shape of Chart object."""
        return self.to_frame().shape

    @property
    def has_OHLCV(self):
        """Return True if Chart DataFrame has OHLCV, False otherwise."""
        cols = {self.op, self.hi, self.lo, self.cl, self.vo}
        arr = self.df.columns.isin(cols)
        return np.sum(arr) >= len(cols)

    @property
    def has_OHLC(self):
        """Return True if Chart DataFrame has OHLC, False otherwise."""
        cols = {self.op, self.hi, self.lo, self.cl}
        arr = self.df.columns.isin(cols)
        return np.sum(arr) >= len(cols)

    @property
    def has_open(self):
        """Return True if Chart DataFrame has open, False otherwise."""
        if self.op in self.df.columns:
            return True
        else:
            return False

    @property
    def has_high(self):
        """Return True if Chart DataFrame has high, False otherwise."""
        if self.hi in self.df.columns:
            return True
        else:
            return False

    @property
    def has_low(self):
        """Return True if Chart DataFrame has low, False otherwise."""
        if self.lo in self.df.columns:
            return True
        else:
            return False
    @property
    def has_close(self):
        """Return True if Chart DataFrame has close, False otherwise."""
        if self.cl in self.df.columns:
            return True
        else:
            return False

    @property
    def has_volume(self):
        """Return True if Chart DataFrame has volume, False otherwise."""
        if self.vo in self.df.columns:
            return True
        else:
            return False

    def adjust(self, inplace=False):
        """Adjust OHLC data for splits, dividends, etc.

        Requires an adjusted close column to adjust the rest of the OHLC bars.

        Parameters
        ----------
            inplace : bool
                Modifies Chart inplace (returns None) if True, else
                returns modified Chart by default.

        """

        """ADD ERROR HANDLING"""

        ratio = (self.df[self.cl] / self.df[self.acl])

        if inplace:
            self.df[self.op] = self.df[self.op] / ratio
            self.df[self.hi] = self.df[self.hi] / ratio
            self.df[self.lo] = self.df[self.lo] / ratio
            self.df[self.cl] = self.df[self.cl] / ratio
        else:
            df2 = self.df.copy()
            df2[self.op] = self.df[self.op] / ratio
            df2[self.hi] = self.df[self.hi] / ratio
            df2[self.lo] = self.df[self.lo] / ratio
            df2[self.cl] = self.df[self.cl] / ratio
            return Chart(df2)

    def adjust_volume(self, inplace=False):
        """Adjust volume data for splits, dividends, etc.

        Requires a close and and adjusted close column to adjust volume.

        Parameters
        ----------
            inplace : bool
                Modifies Chart inplace (returns None) if True, else
                returns modified Chart by default.

        """

        """ADD ERROR HANDLING"""

        ratio = (self.df[self.cl] / self.df[self.acl])

        if inplace:
            self.df[self.vo] = self.df[self.vo] / ratio
        else:
            df2 = self.df.copy()
            df2[self.vo] = self.df[self.vo] / ratio
            return Chart(df2)

    def to_frame(self):
        """Return DataFrame representation of Chart, including all added
        technical indicators."""
        return self.df.join([self.ind])

    def to_figure(self, type=None, volume=None,
                  theme=None, layout=None,
                  title=None, hovermode=None,
                  legend=None, annotations=None, shapes=None,
                  dimensions=None, width=None, height=None, margin=None,
                  **kwargs):
        """Return Plotly figure (dict) that is used to generate the stock chart.

        Parameters
        ----------

        """
        # Check for kwargs integrity
        for key in kwargs:
            if key not in VALID_FIGURE_KWARGS:
                raise Exception("Invalid keyword '{0}'.".format(key))

        # Kwargs
        if 'kind' in kwargs:
            type = kwargs['kind']

        if 'showlegend' in kwargs:
            legend = kwargs['showlegend']

        if 'figsize' in kwargs: # Matplotlib
            figsize = kwargs['figsize']
            if isinstance(figsize, tuple) and len(figsize) == 2:
                dimensions = tuple(80 * i for i in figsize) # 80x size
            else:
                raise Exception("Invalid figsize '{0}'.".format(figsize))

        # Default settings
        if type is None:
            if self.has_OHLC:
                type = 'candlestick'
            elif self.has_close:
                type = 'line'
            else:
                raise Exception("Chart has neither OLHC nor close.")

        if volume is None:
            if self.has_volume:
                volume = True
            else:
                volume = False

        if title is None:
            if self.ticker:
                title = ticker
                if self.start and self.end:
                    if isinstance(self.start, str) and isinstance(self.end, str):
                        title = title + ' [{0}/{1}]'.format(self.start, self.end)
            else:
                title = ''

        if legend is None:
            legend = True

        # Check for argument integrity (above checked in get_template)
        if type:
            if not isinstance(type, six.string_types):
                raise Exception("Invalid type '{0}'.".format(type))
                if type not in VALID_TRACES:
                    raise Exception("Invalid keyword '{0}'.".format(type))

        if volume or volume == False:
            if not isinstance(volume, bool):
                raise Exception("Invalid volume'{0}'.".format(title))

        # Get template and bind to colors, traces, additions and layotu
        template = tools.get_template(theme=theme, layout=layout,
                                      title=title,
                                      hovermode=hovermode, legend=legend,
                                      annotations=annotations, shapes=shapes,
                                      dimensions=dimensions,
                                      width=width, height=height,
                                      margin=margin, **kwargs)
        colors = template['colors']
        traces = template['traces']
        additions = template['additions']
        layout = template['layout']

        # Get data
        data = []

        # Plot main chart
        if type == 'candlestick':

            trace = copy.deepcopy(traces['candlestick'])

            trace['x'] = self.df.index
            trace['open'] = self.df[self.op]
            trace['high'] = self.df[self.hi]
            trace['low'] = self.df[self.lo]
            trace['close'] = self.df[self.cl]
            trace['name'] = title
            trace['yaxis'] = 'y1'
            trace['showlegend'] = False

            # Colors
            trace['increasing']['fillcolor'] = colors['increasing']
            trace['increasing']['line']['color'] = colors['border']

            trace['decreasing']['fillcolor'] = colors['decreasing']
            trace['decreasing']['line']['color'] = colors['border']

            data.append(trace)

        elif 'line' in type:

            trace = copy.deepcopy(traces[type])

            trace['x'] = self.df.index
            trace['y'] = self.df[self.cl]
            trace['name'] = title
            trace['yaxis'] = 'y1'
            trace['showlegend'] = False

            # Colors
            trace['line']['color'] = colors['primary']

            data.append(trace)

        elif 'area' in type:

            trace = copy.deepcopy(traces[type])

            trace['x'] = self.df.index
            trace['y'] = self.df[self.cl]
            trace['name'] = title
            trace['yaxis'] = 'y1'
            trace['showlegend'] = False

            # Colors
            trace['line']['color'] = colors['primary']

            data.append(trace)

        elif 'scatter' in type:

            trace = copy.deepcopy(traces[type])

            trace['x'] = self.df.index
            trace['y'] = self.df[self.cl]
            trace['name'] = title
            trace['yaxis'] = 'y1'
            trace['showlegend'] = False

            # Colors
            trace['scatter']['color'] = colors['primary']

            data.append(trace)

        else:
            raise Exception("Cannot plot this chart type '{0}'.".format(type))

        # Plot primary indicators
        for name in self.pri:

            primary = self.pri[name]
            trace = copy.deepcopy(traces[primary['type']])

            trace['x'] = self.ind.index
            trace['y'] = self.ind[name]
            trace['name'] = name
            trace['yaxis'] = 'y1'

            # Colors
            trace['line']['color'] = colors[primary['color']]

            if 'area' in primary['type']:
                if 'fillcolor' in primary:
                    trace['fillcolor'] = colors[primary['fillcolor']]

            data.append(trace)

        # Plot volume
        if volume:

            trace = copy.deepcopy(traces['bar'])
            trace['x'] = self.df.index
            trace['y'] = self.df[self.cl]
            trace['name'] = 'Volume'
            trace['yaxis'] = 'y2'
            trace['showlegend'] = False

            # Determine if volume should be in 2 colors or in 1
            if type == 'candlestick' and self.has_open and self.has_close:
                volume_color = [
                    colors['increasing']
                    if (value - self.df[self.op].values[i]) >= 0
                    else colors['decreasing']
                    for i, value in enumerate(self.df[self.cl].values)
                ]
            else:
                volume_color = colors['primary']

            trace['marker']['color'] = volume_color
            trace['marker']['line']['color'] = colors['border']

            data.append(trace)

        # Subplot volume delta
        if volume:
            delta = 1
        else:
            delta = 0

        # Plot secondary indicators
        for i, name in enumerate(self.sec):

            secondary = self.sec[name]
            trace = copy.deepcopy(traces[secondary['type']])

            trace['x'] = self.ind.index
            trace['y'] = self.ind[name]
            trace['name'] = name
            trace['yaxis'] = 'y' + str(i + delta + 2)

            trace['line']['color'] = colors[secondary['color']]

            if 'area' in secondary['type']:
                if 'fillcolor' in secondary:
                    trace['fillcolor'] = colors[secondary['fillcolor']]

            data.append(trace)

        # Modify layout

        # Margin
        if not title:
            layout['margin']['t'] = layout['margin']['b']

        if legend == True:
            if annotations == None:
                layout['legend']['y'] -= 0.02
                annotation = dict(
                    x = layout['legend']['x'],
                    xanchor = layout['legend']['xanchor'],
                    xref = 'paper',
                    y = layout['legend']['y'] + 0.02,
                    yanchor = layout['legend']['yanchor'],
                    yref = 'paper',
                    showarrow = False,
                    text = 'TEMPORARY'
                )
                layout['annotations'] = [annotation]

        # Axis
        layout['xaxis'] = copy.deepcopy(additions['xaxis'])
        layout['yaxis'] = copy.deepcopy(additions['yaxis'])

        # Subaxis
        if volume or self.sec:

            if len(self.sec) + delta == 1:
                layout['yaxis2'] = copy.deepcopy(additions['yaxis'])
                layout['yaxis']['domain'] = [0.30, 1.0]
                layout['yaxis2']['domain'] = [0.0, 0.25]

            elif len(self.sec) + delta == 2:
                layout['yaxis2'] = copy.deepcopy(additions['yaxis'])
                layout['yaxis3'] = copy.deepcopy(additions['yaxis'])
                layout['yaxis']['domain'] = [0.5, 1.0]
                layout['yaxis2']['domain'] = [0.25, 0.45]
                layout['yaxis3']['domain'] = [0.0, 0.20]

            else:
                print('Quantmod does not yet support plotting 3+ indicators.')

        figure = dict(data=data, layout=layout)
        return figure

    def plot(self, type=None, volume=None,
             theme=None, layout=None,
             title=None, hovermode=None,
             legend=None, annotations=None, shapes=None,
             dimensions=None, width=None, height=None, margin=None,
             **kwargs):
        """Generate a Plotly chart from Chart specifications.

        Parameters
        ----------

        """
        figure = self.to_figure(type=type, volume=None, theme=theme,
                                layout=layout, title=title,
                                hovermode=hovermode, legend=legend,
                                annotations=annotations, shapes=shapes,
                                dimensions=dimensions,
                                width=width, height=height,
                                margin=margin, **kwargs)
        return py.plot(figure)


"""Overlap studies"""
def _SMA(self, timeperiod=30):
    """Simple moving average."""
    name = 'SMA({})'.format(str(timeperiod))
    self.pri[name] = dict(type='line', color='primary')
    self.ind[name] = talib.SMA(self.df[self.cl].values, timeperiod)


def _EMA(self, timeperiod=30):
    """Exponential moving average."""
    name = 'EMA({})'.format(str(timeperiod))
    self.pri[name] = dict(type='line', color='primary')
    self.ind[name] = talib.EMA(self.df[self.cl].values, timeperiod)


def _WMA(self, timeperiod=30):
    """Weighted moving average."""
    name = 'WMA({})'.format(str(timeperiod))
    self.pri[name] = dict(type='line', color='primary')
    self.ind[name] = talib.WMA(self.df[self.cl].values, timeperiod)


def _DEMA(self, timeperiod=30):
    """Double exponential moving average."""
    name = 'DEMA({})'.format(str(timeperiod))
    self.pri[name] = dict(type='line', color='primary')
    self.ind[name] = talib.DEMA(self.df[self.cl].values, timeperiod)


def _TEMA(self, timeperiod=30):
    """Triple moving exponential average."""
    name = 'TEMA({})'.format(str(timeperiod))
    self.pri[name] = dict(type='line', color='primary')
    self.ind[name] = talib.TEMA(self.df[self.cl].values, timeperiod)


def _KAMA(self, timeperiod=30):
    """Kaufmann adaptive moving average."""
    name = 'KAMA({})'.format(str(timeperiod))
    self.pri[name] = dict(type='line', color='primary')
    self.ind[name] = talib.KAMA(self.df[self.cl].values, timeperiod)


def _TRIMA(self, timeperiod=30):
    """Triangular moving average."""
    name = 'TRIMA({})'.format(str(timeperiod))
    self.pri[name] = dict(type='line', color='primary')
    self.ind[name] = talib.TRIMA(self.df[self.cl].values, timeperiod)


def _MA(self, timeperiod=30, matype=0):
    """Moving average (customizable)."""
    name = 'MA({})'.format(str(timeperiod))
    self.pri[name] = dict(type='line', color='primary')
    self.ind[name] = talib.MA(self.df[self.cl].values, timeperiod, matype)


def _BBANDS(self, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0):
    """Bollinger bands."""
    name = 'BB({},{},{})'.format(str(timeperiod), str(nbdevup), str(nbdevdn))
    ubb = 'U' + name
    bb = name
    lbb = 'L' + name
    self.pri[ubb] = dict(type='line_dashed_thin', color='secondary')
    self.pri[bb] = dict(type='area_dashed_thin', color='grey', fillcolor='fill')
    self.pri[lbb] = dict(type='area_dashed_thin', color='secondary', fillcolor='fill')
    self.ind[ubb], self.ind[bb], self.ind[lbb] = talib.BBANDS(self.df[self.cl].values,
                                                              timeperiod, nbdevup, nbdevdn, matype)


def _MAMA(self):
    pass


def _MAVP(self, periods, inperiod=2, maxperiod=30, matype=0):
    pass


def _RSI(self, timeperiod=14):
    name = 'RSI({})'.format(str(timeperiod))
    self.sec[name] = dict(type='line', color='primary')
    self.ind[name] = talib.RSI(self.df[self.cl].values, timeperiod)


Chart.add_SMA = _SMA
Chart.add_EMA = _EMA
Chart.add_WMA = _WMA
Chart.add_DEMA = _DEMA
Chart.add_TEMA = _TEMA
Chart.add_KAMA = _KAMA
Chart.add_TRIMA = _TRIMA
Chart.add_MA = _MA
#Chart.add_MAMA = _MAMA
#Chart.add_MAVP = _MAVP
Chart.add_BBANDS = _BBANDS
#Chart.SAR = _SAR
#Chart.SAREXT = _SAREXT
#Chart.HT_TRENDLINE = _HT_TRENDLINE
#Chart.T3 = _T3
#Chart.add_midpoint =

Chart.add_RSI = _RSI
#Chart.ADX = _ADX
#Chart.ADXR = _ADXR
#Chard.APO = _APO
