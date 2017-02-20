import numpy as np
import pandas as pd
import pandas_datareader.data as web
import talib
import plotly.plotly as py
import plotly.offline as pyo
from .themes.themes import get_light_theme


class Chart(object):

    def __init__(self, df, source='yahoo'):

        self.df = df

        self.source = source
        if self.source == 'yahoo':
            op = 'Open'
            hi = 'High'
            lo = 'Low'
            cl = 'Close'
            aop = None
            ahi = None
            alo = None
            acl = 'Adj Close'
            vo = 'Volume'
            di = None

        self.op = op
        self.hi = hi
        self.lo = lo
        self.cl = cl
        self.aop = aop
        self.ahi = ahi
        self.alo = alo
        self.acl = acl
        self.vo = vo
        self.di = di

        self.primary = pd.DataFrame([])
        self.secondary = pd.DataFrame([])

    @property
    def has_open(self):
        return np.fromiter((self.op == column for column in self.df.columns), dtype=np.bool_)
    @property
    def has_high(self):
        return np.fromiter((self.hi == column for column in self.df.columns), dtype=np.bool_)
    @property
    def has_low(self):
        return np.fromiter((self.lo == column for column in self.df.columns), dtype=np.bool_)
    @property
    def has_close(self):
        return np.fromiter((self.cl == column for column in self.df.columns), dtype=np.bool_)

    @property
    def has_adjusted_open(self):
        return np.fromiter((self.aop == column for column in self.df.columns), dtype=np.bool_)
    @property
    def has_adjusted_high(self):
        return np.fromiter((self.ahi == column for column in self.df.columns), dtype=np.bool_)
    @property
    def has_adjusted_low(self):
        return np.fromiter((self.alo == column for column in self.df.columns), dtype=np.bool_)
    @property
    def has_adjusted_close(self):
        return np.fromiter((self.acl == column for column in self.df.columns), dtype=np.bool_)

    @property
    def has_volume(self):
        return np.fromiter((self.vo == column for column in self.df.columns), dtype=np.bool_)
    @property
    def has_dividend(self):
        return np.fromiter((self.di == column for column in self.df.columns), dtype=np.bool_)

    @property
    def is_OHLC(self):
        return not (self.df.filter(like=[self.aop, self.ahi, self.alo, self.acl]).empty)
    @property
    def has_OHLC(self):
        return (np.array(self.has_open) + np.array(self.has_high) + np.array(self.has_low) + np.array(self.has_close))
    @property
    def is_line(self):
        return not (self.df.filter(like=self.cl).empty and self.df.filter(like=self.acl).empty)
    @property
    def has_OHLC(self):
        return (np.array(self.has_close) + np.array(self.has_adjusted_close))


    def adjust(self, inplace=False):

        ratio = (self.df[self.cl]/self.df[self.ad])
        if inplace:
            self.df[self.op] = self.df[self.op] / ratio
            self.df[self.hi] = self.df[self.hi] / ratio
            self.df[self.lo] = self.df[self.lo] / ratio
            self.df[self.cl] = self.df[self.cl] / ratio
            #self.df = self.df.div(ratio, axis='index')
        else:
            df2 = self.df.copy()
            df2[self.op] = self.df[self.op] / ratio
            df2[self.hi] = self.df[self.hi] / ratio
            df2[self.lo] = self.df[self.lo] / ratio
            df2[self.cl] = self.df[self.cl] / ratio
            #df2 = self.df.div(ratio, axis='index')
            return Chart(df2)


    def adjust_volume(self, inplace=False):
        ratio = (self.df[self.cl]/self.df[self.ad])
        if inplace:
            self.df[self.vo] = self.df[self.vo] / ratio
        else:
            df2 = self.df.copy()
            df2[self.vo] = self.df[self.vo] / ratio
            return Chart(df2)


    def to_frame(self):
        return self.df.join([self.primary, self.secondary])


    def add(self, function, **kwargs):

        inputs = dict(
            open = self.df[self.op],
            high = self.df[self.hi],
            low = self.df[self.lo],
            close = self.df[self.cl],
            volume = self.df[self.vo],
        )
        self.primary = function(inputs, **kwargs)


    def plot(self, type='candlestick', title='Stock'):

        template, layout = get_light_theme()

        data = []
        if type == 'candlestick':

            candlestick = template['candlestick']

            candlestick['x'] = self.df.index
            candlestick['open'] = self.df[self.op]
            candlestick['high'] = self.df[self.hi]
            candlestick['low'] = self.df[self.lo]
            candlestick['close'] = self.df[self.cl]
            candlestick['name'] = title
            candlestick['yaxis'] = 'y1'

            data.append(candlestick)

        elif type == 'line':

            line = template['line']

            line['x'] = self.df.index
            line['y'] = self.df[self.ad]
            line['name'] = title
            line['yaxis'] = 'y1'

            data.append(line)

        for i, column in enumerate(self.primary):

            line = template['line']

            line['x'] = self.df.index
            line['y'] = self.primary[column]
            line['name'] = self.primary.columns[i]
            line['yaxis'] = 'y1'

            data.append(line)

        for i, column in enumerate(self.secondary):

            line = template['line']

            line['x'] = self.df.index
            line['y'] = self.secondary[column]
            line['name'] = self.secondary.columns[i]
            line['yaxis'] = 'y2'

            data.append(line)

        layout['xaxis'] = template['xaxis']
        layout['yaxis'] = template['yaxis']
        layout['title'] = title

        if len(self.secondary.columns):
            layout['yaxis2'] = template['yaxis2']
            layout['yaxis1']['domain'] = [0.3, 1.0]
            layout['yaxis2']['domain'] = [0.0, 0.2]

        figure = dict(data=data, layout=layout)
        return py.plot(figure)

# ta.py

def _MA(self, timeperiod=30, matype=0):
    name = 'MA({})'.format(str(timeperiod))
    self.primary[name] = talib.MA(self.df[self.cl].values, timeperiod, matype)

def _SMA(self, timeperiod=30):
    name = 'SMA({})'.format(str(timeperiod))
    self.primary[name] = talib.SMA(self.df[self.cl].values, timeperiod)

def _EMA(self, timeperiod=30):
    name = 'EMA({})'.format(str(timeperiod))
    self.primary[name] = talib.EMA(self.df[self.cl].values, timeperiod)

def _BBANDS(self, timperiod=5, nbdevup=2, nbdevdn=2, matype=0):
    name = 'BB({}, {}, {})'.format(str(timeperiod), str(nbdevup), str(nbdevdn))
    upperband = name + ' Upper'
    middleband = name + ' Middle'
    lowerband = name + ' Lower'
    self.primary[upperband], self.primary[middleband], self.primary[lowerband] = talib.BBANDS(self.df[self.cl], timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)

#def _RSI(self, )[ for value in variable]

Chart.add_MA = _MA
Chart.add_SMA = _SMA
Chart.add_EMA = _EMA

Chart.add_BBANDS = _BBANDS
#Chart.add_RSI = _RSI

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

# tests.py

#ticker = 'AAPL'

#template, layout = get_light_theme()

#df = web.DataReader(ticker, data_source='yahoo')
#ch = Chart(df)
#ch = ch.adjust()
#ch.add_MA(50)
#ch.to_frame()
#ch.primary.columns
#ch.SMA(50)
#ch.EMA(200)
#ch.plot()
