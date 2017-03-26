
# In[]:

import quantmod as qm
import pandas as pd
import pandas_datareader as web


# In[]:

ticker = 'AAPL'
df = web.DataReader(ticker, data_source='yahoo')
df = df.head(365)
ch = qm.Chart(df, start='2015/01/01', end='2017/03/02')
ch.to_frame()

#del df['Close']
#del df['Adj Close']
#del ch.df['Open']

ch.has_open
ch.has_high
ch.has_low
ch.has_close
ch.op
ch.df
ch.ind
ch.pri
ch.adjust(inplace=True)
ch.adjust_volume(inplace=True)

ch.has_OHLC
print(ch.has_OHLCV)

#ch.add_MA(50)
#ch.add_SMA(50)
#ch.add_EMA(200)
ch.add_BBANDS(30)
ch.add_RSI(14)

qm.go_offline()
ch.to_figure()
#qm.go_online()
#ch.plot(title=False)
ch.plot(dimensions=(2560,1440))
