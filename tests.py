
# In[]:
import quantmod.offline as qmo
import quantmod.chart as qm
import quantmod.tools as qmt
import pandas as pd
import pandas_datareader as web


# In[]:
ticker = 'AAPL'
#template, layout = get_light_theme()
df = web.DataReader(ticker, data_source='yahoo')
df = df.tail(365)
ch = qm.Chart(df, start='2015/01/01', end='2017/03/02')
ch.has_close
ch.to_frame()
#del df['Close']
#del df['Adj Close']
#del ch.df['Open']
#ch.has_open
ch.has_close
#ch.has_adjusted_close
ch.op
ch.df
ch.ind
ch.pri
ch.adjust(inplace=True)
ch.has_OHLC
print(ch.has_OHLCV)
#ch.add_MA(50)
#ch.add_SMA(50)
#ch.add_EMA(200)
ch.add_BBANDS(30)
#ch.add_RSI(14)
#ch.add_RSI(25)
ch.ind
ch.pri
#qmo.go_offline()
qmt.get_template()
#ch.to_figure()
ch.plot(title=False)
