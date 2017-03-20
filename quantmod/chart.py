"""Main Chart() functionnality.

Includes Quantmod plotting engine.

"""
from __future__ import absolute_import

import copy
import numpy as np
import pandas as pd
import plotly.plotly as py
import plotly.offline as pyo

import talib # To be removed

from . import utils
from . import tools


class Chart(object):
    """Quantmod's Chart() object based on a df.

    BLABLABLA

    """
    def __init__(self, df, source='yahoo'):

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

    @property
    def has_open(self):

        cols = {self.op}
        return self.df.columns.isin(cols)
    @property
    def has_high(self):

        cols = {self.hi}
        return self.df.columns.isin(cols)
    @property
    def has_low(self):

        cols = {self.lo}
        return self.df.columns.isin(cols)
    @property
    def has_close(self):

        cols = {self.cl}
        return self.df.columns.isin(cols)
    @property
    def has_adjusted_close(self):

        cols = {self.acl}
        return self.df.columns.isin(cols)

    @property
    def has_volume(self):

        cols = {self.vo}
        return self.df.columns.isin(cols)
    @property
    def has_dividend(self):

        cols = {self.di}
        return self.df.columns.isin(cols)

    @property
    def has_OHLC(self):

        cols = {self.op, self.hi, self.lo, self.cl}
        return self.df.columns.isin(cols)
    @property
    def has_line(self):

        cols = {self.cl}
        return self.df.columns.isin(cols)

    @property
    def is_OHLC(self):
        """Return True if Chart() supports OHLC, False otherwise."""
        cols = {self.op, self.hi, self.lo, self.cl}
        arr = self.df.columns.isin(cols)
        return np.sum(arr) >= len(cols)
    @property
    def is_line(self):
        """Return True if Chart() supports line, False otherwise."""
        cols = {self.cl}
        arr = self.df.columns.isin(cols)
        return np.sum(arr) >= len(cols)


    def adjust(self, inplace=False):

        ratio = (self.df[self.cl]/self.df[self.acl])
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
        ratio = (self.df[self.cl]/self.df[self.acl])
        if inplace:
            self.df[self.vo] = self.df[self.vo] / ratio
        else:
            df2 = self.df.copy()
            df2[self.vo] = self.df[self.vo] / ratio
            return Chart(df2)


    def to_frame(self):
        return self.df.join([self.ind])


    def plot(self, type='candlestick', title='Stock'):

        template = tools.make_template()
        colors = template['colors']
        traces = template['traces']
        additions = template['additions']
        layout = template['layout']

        data = []

        for column in self.pri:

            trace = copy.deepcopy(traces[self.pri[column]['type']])

            trace['x'] = self.ind.index
            trace['y'] = self.ind[column]
            trace['name'] = column
            trace['yaxis'] = 'y1'

            #COLORS
            trace['line']['color'] = colors[self.pri[column]['color']]
            if 'fillcolor' in self.pri[column]:
                trace['fillcolor'] = colors[self.pri[column]['fillcolor']]

            data.append(trace)

        if type == 'candlestick':

            trace = copy.deepcopy(traces['candlestick'])

            trace['x'] = self.df.index
            trace['open'] = self.df[self.op]
            trace['high'] = self.df[self.hi]
            trace['low'] = self.df[self.lo]
            trace['close'] = self.df[self.cl]
            trace['name'] = title
            trace['yaxis'] = 'y1'

            # COLORS
            trace['increasing']['line']['color'] = colors['increasing']
            trace['decreasing']['line']['color'] = colors['decreasing']

            data.append(trace)

        if type == 'line':

            trace = copy.deepcopy(traces['line'])

            trace['x'] = self.df.index
            trace['y'] = self.df[self.cl]
            trace['name'] = title
            trace['yaxis'] = 'y1'

            data.append(trace)

        for column in self.sec:

            trace = copy.deepcopy(traces[self.sec[column]['type']])

            trace['x'] = self.ind.index
            trace['y'] = self.ind[column]
            trace['name'] = column
            trace['yaxis'] = 'y2'

            data.append(trace)

        layout['xaxis'] = additions['xaxis'].copy()
        layout['yaxis'] = additions['yaxis'].copy()

        if self.sec:
            layout['yaxis2'] = additions['yaxis'].copy()
            layout['yaxis']['domain'] = [0.3, 1.0]
            layout['yaxis2']['domain'] = [0.0, 0.2]

        figure = dict(data=data, layout=layout)
        return py.plot(figure)

# ta.py

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
    self.pri[upperband] = dict(type='line_dashed', color='primary')
    self.pri[middleband] = dict(type='area_dashed', color='secondary', fillcolor='background')
    self.pri[lowerband] = dict(type='area_dashed', color='primary', fillcolor='background')
    self.ind[upperband], self.ind[middleband], self.ind[lowerband] = talib.BBANDS(self.df[self.cl].values, timeperiod, nbdevup, nbdevdn, matype)

def _RSI(self, timeperiod=14):
    name = 'RSI({})'.format(str(timeperiod))
    self.sec[name] = dict(type='line')
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
