import pandas as pd
import pandas_datareader.data as web
import talib
from talib import abstract

import plotly.plotly as py
import plotly.offline as pyo


class Chart(object):

    def __init__(self, df, source='yahoo'):

        self.df = df

        self.source = source
        if self.source == 'yahoo':
            op = 'Open'
            hi = 'High'
            lo = 'Low'
            cl = 'Close'
            ad = 'Adj Close'
            vo = 'Volume'

        self.op = op
        self.hi = hi
        self.lo = lo
        self.cl = cl
        self.ad = ad
        self.vo = vo

        self.primary = pd.DataFrame(index = df.index)
        self.secondary = pd.DataFrame(index = df.index)


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


    def plot(self, type='candlestick', title='Stock', theme='light'):

        data = []
        if type == 'candlestick':
            data.append(
                dict(
                    type = 'candlestick',
                    x = self.df.index,
                    open = self.df[self.op],
                    high = self.df[self.hi],
                    low = self.df[self.lo],
                    close = self.df[self.cl],
                    name = title,
                    yaxis = 'y1',
                )
            )
        elif type == 'line':
            data.append(
                dict(
                    type = 'scatter',
                    mode = 'lines',
                    x = self.df.index,
                    y = self.df[self.ad],
                    name = title,
                    yaxis = 'y1',
                )
            )

        for column in self.primary:
            data.append(
                dict(
                    type = 'scatter',
                    mode = 'lines',
                    x = self.df.index,
                    y = self.primary[column],
                    name = column,
                    yaxis = 'y1',
                )
            )

        for column in self.secondary:
            data.append(
                dict(
                    type = 'scatter',
                    mode = 'lines',
                    x = self.df.index,
                    y = self.secondary[column],
                    name = column,
                    yaxis = 'y2',
                )
            )

        layout = dict(
            title = ticker,

            font = dict(family = 'overpass'),
            showlegend = False,
            yaxis = dict(
                domain = [0.0, 1.0],
                type = 'linear',
            ),
            xaxis = dict(
                rangeslider = dict(
                    visible = False,
                ),
            ),
        )
        if len(self.secondary.columns):
            layout['yaxis1']['domain'] = [0.3, 1.0]
            layout['yaxis2']['domain'] = [0.0, 0.2]

        if theme == 'light':
            layout['plot_bgcolor'] = '#FAFAFA'
            layout['paper_bgcolor'] = '#F5F6F9'

        figure = dict(data=data, layout=layout)
        return py.plot(figure)

def _MA(self, timeperiod=30):
    name = 'MA({})'.format(str(timeperiod))
    self.primary[name] = talib.MA(self.df[self.cl].values, timeperiod)

def _SMA(self, timeperiod=30):
    name = 'SMA({})'.format(str(timeperiod))
    self.primary[name] = talib.SMA(self.df[self.cl].values, timeperiod)

def _EMA(self, timeperiod=30):
    name = 'EMA({})'.format(str(timeperiod))
    self.primary[name] = talib.EMA(self.df[self.cl].values, timeperiod)



Chart.MA = _MA
Chart.SMA = _SMA
Chart.EMA = _EMA
#Chart.BBANDS = _BBANDS
#Chart.RSI = _RSI

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


# In[]:
ticker = 'AAPL'

df = web.DataReader(ticker, data_source='yahoo')
ch = Chart(df)
sma = abstract.SMA
ch.add(sma)
ch.adjust(inplace=True)
ch.MA(50)
ch.SMA(50)
ch.EMA(200)
ch.plot()
