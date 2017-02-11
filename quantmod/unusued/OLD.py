from plotly.graph_objs import *
from plotly.tools import FigureFactory as FF
import pandas_datareader.data as web
import datetime as dt
from stlib.service.strategy.random import RandomStrategy

class Data():
    def __init__(self, ticker, start='1900'):
        self.ticker = ticker
        self.start = start
        self.period = '-1'
        self.adjust_close = True
        self.df = None
        self.plot_data = None
        self.transactions =5
        self.strategies =[RandomStrategy(self.plot_data, self.transactions)]

    def calc(self):
        for strategy in self.strategies:
            strategy.data = self.plot_data
            strategy.run()


    def load(self):
        print "loading " , self.ticker
        data = web.DataReader(self.ticker, data_source='yahoo', start=self.start)
        data = data.rename(columns={'Open': 'O', 'High': 'H', 'Low': 'L', 'Close': 'C', 'Adj Close': 'AC','Volume': 'V'})
        if self.adjust_close:
            adj = data['AC'] - data['C']
            data['O'] += adj
            data['H'] += adj
            data['L'] += adj
            data['C'] += adj
            data = data.drop('AC', axis=1)
            data['S5'] = data['C'].rolling(5).mean()
            data['S10'] = data['C'].rolling(10).mean()
            data['S15'] = data['C'].rolling(15).mean()
            data['S30'] = data['C'].rolling(30).mean()
            data['S50'] = data['C'].rolling(50).mean()
            data['S100'] = data['C'].rolling(100).mean()
            data['S200'] = data['C'].rolling(200).mean()

        self.df = data
        self.getPeriod('100d')
        self.calc()

    def buildShapes(self):
        shapes =[]
        for strategy in self.strategies:
            result = strategy.result

            for (buy, sell) in result:
                 params = {'y0':0,'y1':1,'xref':'x','yref':'paper','line':{'color': 'rgb(60,160,160)','width':1}}
                 params['x0'] = self.plot_data.index[buy]
                 params['x1'] = self.plot_data.index[buy]
                 shapes.append(params)

                 params1= {'y0':0,'y1':1,'xref':'x','yref':'paper','line':{'color': 'rgb(160,60,60)','width':1}}
                 params1['x0'] = self.plot_data.index[sell]
                 params1['x1'] = self.plot_data.index[sell]
                 shapes.append(params1)


        return shapes

    def plot(self):
        fig = FF.create_candlestick(self.plot_data.O, self.plot_data.H, self.plot_data.L, self.plot_data.C, dates=self.plot_data.index)
        shapes = self.buildShapes()

        fig['layout'].update({'title': self.ticker,
                              'yaxis': {'title': 'Price'},
                              'xaxis': {'title': 'Date'},
                              'shapes': shapes

                             })

        close_line = Scatter(x=self.plot_data.index, y=self.plot_data.C,name='Close',line={'shape':'spline'})
        sma5_line = Scatter(x=self.plot_data.index, y=self.plot_data.S5,name='SMA5',line={'shape':'spline','dash':'dot'})
        sma10_line = Scatter(x=self.plot_data.index, y=self.plot_data.S10,name='SMA10', line={'shape':'spline','dash':'dot'})
        sma15_line = Scatter(x=self.plot_data.index, y=self.plot_data.S15,name='SMA15', line={'shape':'spline','dash':'dot'})
        sma30_line = Scatter(x=self.plot_data.index, y=self.plot_data.S15,name='SMA30', line={'shape':'spline','dash':'dot'})
        sma50_line = Scatter(x=self.plot_data.index, y=self.plot_data.S30,name='SMA50', line={'shape':'spline','dash':'dot'})
        sma100_line = Scatter(x=self.plot_data.index, y=self.plot_data.S50,name='SMA100', line={'shape':'spline','dash':'dot'})
        sma200_line = Scatter(x=self.plot_data.index, y=self.plot_data.S100,name='SMA200', line={'shape':'spline','dash':'dot'})
        volume = Bar(x = self.plot_data.index, y = self.plot_data.V/50000000.0, name='Volume')
        fig['data'].extend([close_line,sma5_line,sma10_line,sma15_line,sma30_line, sma50_line, sma100_line, sma200_line, volume])
        return fig
    pass



    def getPeriod(self, period='-1'):
        if period == '-1':
            period = self.period
        else:
            self.period = period

        if period=='-1':
            self.plot_data = self.df
            return

        now = dt.date.today()

        if (period[-1]=='y'):
            factor = 365
        elif (period[-1]=='m'):
            factor = 30
        elif (period[-1]=='w'):
            factor = 7
        elif (period[-1]=='d'):
            factor = 1
        else:
            start = self.df.index.searchsorted(dt.date(period, 1, 1))
            end = self.df.index.searchsorted(dt.date(period+1,1,1))
            self.plot_data = self.df[start:end]
            return

        t = dt.timedelta(int(period[:-1])*factor)
        start = self.df.index.searchsorted(now-t)
        end = self.df.index.searchsorted(now)
        self.plot_data = self.df[start:end]
        return
