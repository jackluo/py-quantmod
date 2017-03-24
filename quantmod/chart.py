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

from . import utils
from . import tools
from .tools import _VALID_TRACES


_VALID_FIGURE_KWARGS = {'kind'}  # Alternative for type


class Chart(object):
    """Quantmod Chart based on Pandas DataFrame.

    Features include time series adjustement, volume adjustement, and plotting.

    """

    def __init__(self, df, source='yahoo', columns=None):
        """ADD INFO

        ADD DOCUMENTATION

        """

        """ADD ERROR HANDLING"""

        self.df = df

        self.source = source
        if self.source == 'yahoo':
            op = 'Open'
            hi = 'High'
            lo = 'Low'
            cl = 'Close'
            acl = 'Adj Close'
            vo = 'Volume'
            di = None

        self.op = op
        self.hi = hi
        self.lo = lo
        self.cl = cl
        self.acl = acl
        self.vo = vo
        self.di = di

        self.ind = pd.DataFrame([], index=self.df.index)
        self.pri = {}
        self.sec = {}

    def __repr__(self):
        """Return representation of string object."""
        return str(self.to_frame())

    def __len__(self):
        """Return length of Chart object."""
        return len(self.to_frame())

    @property
    def shape(self):
        """Return shape of Chart object."""
        return self.to_frame().shape

    @property
    def has_open(self):
        """Return elementwise boolean np.ndarray.
        True if column has low, False otherwise.

        Example
        -------
            has_open()
                >>> np.ndarray(True, False, False, False, False, dtype=bool)

        """
        cols = {self.op}
        return self.df.columns.isin(cols)

    @property
    def has_high(self):
        """Return elementwise boolean np.ndarray:
        True if column has high, False otherwise.

        """
        cols = {self.hi}
        return self.df.columns.isin(cols)

    @property
    def has_low(self):
        """Return elementwise boolean np.ndarray:
        True if column has low, False otherwise.

        """
        cols = {self.lo}
        return self.df.columns.isin(cols)

    @property
    def has_close(self):
        """Return elementwise boolean np.ndarray:
        True if column has close, False otherwise.

        """
        cols = {self.cl}
        return self.df.columns.isin(cols)

    @property
    def has_adjusted_close(self):
        """Return elementwise boolean np.ndarray:
        True if column has adjusted close, False otherwise.

        """
        cols = {self.acl}
        return self.df.columns.isin(cols)

    @property
    def has_volume(self):
        """Return elementwise boolean np.ndarray:
        True if column has volume, False otherwise.

        """
        cols = {self.vo}
        return self.df.columns.isin(cols)

    @property
    def has_dividend(self):
        """Return elementwise boolean np.ndarray:
        True if column has dividend, False otherwise.

        """
        cols = {self.di}
        return self.df.columns.isin(cols)

    @property
    def has_OHLC(self):
        """Return elementwise boolean np.ndarray:
        True if column has open, high, low or close, False otherwise.

        """
        cols = {self.op, self.hi, self.lo, self.cl}
        return self.df.columns.isin(cols)

    @property
    def has_line(self):
        """Return elementwise boolean np.ndarray:
        True if column has close, False otherwise.

        Same as has_close for now.

        """
        cols = {self.cl}
        return self.df.columns.isin(cols)

    @property
    def is_OHLC(self):
        """Return True if Chart supports OHLC plots, False otherwise."""
        cols = {self.op, self.hi, self.lo, self.cl}
        arr = self.df.columns.isin(cols)
        return np.sum(arr) >= len(cols)

    @property
    def is_line(self):
        """Return True if Chart supports line plots, False otherwise."""
        cols = {self.cl}
        arr = self.df.columns.isin(cols)
        return np.sum(arr) >= len(cols)

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

    def to_figure(self, type=None, theme=None, layout=None,
                  legend=None, hovermode=None,
                  annotations=None, shapes=None, title=None,
                  dimensions=None, width=None, height=None, margin=None,
                  **kwargs):
        """Return Plotly figure (dict) that is used to generate the stock chart.

        Parameters
        ----------

        """
        # Check for kwargs integrity
        if kwargs:
            for key in kwargs:
                if key not in _VALID_FIGURE_KWARGS:
                    raise Exception("Invalid keyword '{0}'.".format(key))

        # Default arguments
        if 'kind' in kwargs:
            type = kwargs['kind']

        if not title:
            title = 'Stock'

        if not legend:
            legend = True

        # Check for argument integrity
        if type:
            if not isinstance(type, six.string_types):
                raise Exception("Invalid type '{0}'.".format(type))

                if type not in _VALID_TRACES:
                    raise Exception("Invalid keyword '{0}'.".format(type))
        else:
            if self.is_OHLC:
                type = 'candlestick'
            elif self.is_line:
                type = 'line'
            else:
                raise Exception("Chart has neither OLHC nor line.")

        # Get template and bind to colors, traces, additions and layotu
        template = tools.get_template(theme, layout,
                                      legend, hovermode,
                                      annotations, shapes, title,
                                      dimensions, width, height, margin,
                                      **kwargs)
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

            # Colors
            trace['increasing']['line']['color'] = colors['grey']
            trace['increasing']['fillcolor'] = colors['increasing']

            trace['decreasing']['line']['color'] = colors['grey']
            trace['decreasing']['fillcolor'] = colors['decreasing']

            data.append(trace)

        elif 'line' in type:
            trace = copy.deepcopy(traces[type])

            trace['x'] = self.df.index
            trace['y'] = self.df[self.cl]
            trace['name'] = title
            trace['yaxis'] = 'y1'

            # Colors
            trace['line']['color'] = colors['primary']

            data.append(trace)

        elif 'area' in type:
            trace = copy.deepcopy(traces[type])

            trace['x'] = self.df.index
            trace['y'] = self.df[self.cl]
            trace['name'] = title
            trace['yaxis'] = 'y1'

            # Colors
            trace['line']['color'] = colors['primary']

            data.append(trace)

        elif 'scatter' in type:
            trace = copy.deepcopy(traces[type])

            trace['x'] = self.df.index
            trace['y'] = self.df[self.cl]
            trace['name'] = title
            trace['yaxis'] = 'y1'

            # Colors
            trace['scatter']['color'] = colors['primary']

            data.append(trace)

        else:
            raise Exception("Cannot plot this chart type '{0}'.".format(type))

        # Plot overlay indicators
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

        # Plot secondary indicators
        for i, name in enumerate(self.sec):

            secondary = self.sec[name]
            trace = copy.deepcopy(traces[secondary['type']])

            trace['x'] = self.ind.index
            trace['y'] = self.ind[name]
            trace['name'] = name
            trace['yaxis'] = 'y' + str(i + 2)

            trace['line']['color'] = colors[secondary['color']]

            if 'area' in secondary['type']:
                if 'fillcolor' in secondary:
                    trace['fillcolor'] = colors[secondary['fillcolor']]

            data.append(trace)

        layout['xaxis'] = copy.deepcopy(additions['xaxis'])
        layout['yaxis'] = copy.deepcopy(additions['yaxis'])

        if self.sec:
            if len(self.sec) == 1:
                layout['yaxis2'] = copy.deepcopy(additions['yaxis'])
                layout['yaxis']['domain'] = [0.30, 1.0]
                layout['yaxis2']['domain'] = [0.0, 0.25]

            if len(self.sec) == 2:
                layout['yaxis2'] = copy.deepcopy(additions['yaxis'])
                layout['yaxis3'] = copy.deepcopy(additions['yaxis'])
                layout['yaxis']['domain'] = [0.5, 1.0]
                layout['yaxis2']['domain'] = [0.25, 0.45]
                layout['yaxis3']['domain'] = [0.0, 0.20]

            else:
                print('Error for now.')

        figure = dict(data=data, layout=layout)
        return figure

    def plot(self, type=None, theme=None, layout=None,
             legend=None, hovermode=None,
             annotations=None, shapes=None, title=None,
             dimensions=None, width=None, height=None, margin=None,
             **kwargs):
        """Generate a Plotly chart of specified Chart.

        ADD DOCUMENTATION.

        """
        figure = self.to_figure(type=type, theme=theme, layout=layout,
                                legend=legend, hovermode=hovermode,
                                annotations=annotations, shapes=shapes,
                                title=title, dimensions=dimensions,
                                width=width, height=height,
                                margin=margin, ** kwargs)
        return py.plot(figure)

""" ta.py """

def _MA(self, timeperiod=30, matype=0):
    name = 'MA({})'.format(str(timeperiod))
    self.pri[name] = dict(type='line', color='primary')
    self.ind[name] = talib.MA(self.df[self.cl].values, timeperiod, matype)


def _SMA(self, timeperiod=30):
    name = 'SMA({})'.format(str(timeperiod))
    self.pri[name] = dict(type='line', color='primary')
    self.ind[name] = talib.SMA(self.df[self.cl].values, timeperiod)


def _EMA(self, timeperiod=30):
    name = 'EMA({})'.format(str(timeperiod))
    self.pri[name] = dict(type='line', color='primary')
    self.ind[name] = talib.EMA(self.df[self.cl].values, timeperiod)


def _BBANDS(self, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0):
    name = 'BB({},{},{})'.format(str(timeperiod), str(nbdevup), str(nbdevdn))
    upperband = 'U' + name
    middleband = name
    lowerband = 'L' + name
    self.pri[upperband] = dict(type='line_dashed_thin', color='secondary')
    self.pri[middleband] = dict(
        type='area_dashed_thin', color='grey', fillcolor='fill')
    self.pri[lowerband] = dict(
        type='area_dashed_thin', color='secondary', fillcolor='fill')
    self.ind[upperband], self.ind[middleband], self.ind[lowerband] = talib.BBANDS(
        self.df[self.cl].values, timeperiod, nbdevup, nbdevdn, matype)


def _RSI(self, timeperiod=14):
    name = 'RSI({})'.format(str(timeperiod))
    self.sec[name] = dict(type='line', color='primary')
    self.ind[name] = talib.RSI(self.df[self.cl].values, timeperiod)

Chart.add_MA = _MA
Chart.add_SMA = _SMA
Chart.add_EMA = _EMA

Chart.add_BBANDS = _BBANDS
Chart.add_RSI = _RSI

#Chart.WMA = _WMA
#Chart.DEMA = _DEMA
#Chart.TEMA = _TEMA
#Chart.KAMA = _KAMA
#Chart.MAVP = _MAVP

#Chart.T3 = _T3
#Chart.SAR = _SAR
#Chart.SAREXT = _SAREXT
#Chart.ADX = _ADX
#Chart.ADXR = _ADXR
#Chard.APO = _APO
#Chart.HT_TRENDLINE = _HT_TRENDLINE
