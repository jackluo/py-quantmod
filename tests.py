# In[]:

import numpy as np
import quantmod as qm
import pandas as pd
import pandas_datareader as web


# In[]:

ticker = 'AAPL'
df = web.DataReader(ticker, data_source='yahoo')
df = df.tail(365)
ch = qm.Chart(df, start='2015/01/01', end='2017/03/02')
# ch = qm.get_symbol('AAPL')
# ch.to_frame()

# del df['Close']
# del df['Adj Close']
# del ch.df['Open']

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

ch.add_MA()
ch.add_SMA()
ch.add_EMA()
ch.add_WMA()
ch.add_DEMA()
ch.add_TEMA()
ch.add_T3()
ch.add_KAMA()
ch.add_TRIMA()
ch.add_MAMA()
# ch.add_MAVP()
ch.add_MIDPOINT()
ch.add_BBANDS()
ch.add_SAR()
ch.add_SAREXT()
ch.add_HT_TRENDLINE()

#ch.add_ADX()
#ch.add_ADXR()
#ch.add_APO()
#ch.add_AROON()
#ch.add_AROONOSC()
#ch.add_BOP()
#ch.add_CCI()
#ch.add_CMO()
#ch.add_DX()
ch.add_MACD()
#ch.add_RSI()
ch.add_MFI()
ch.add_PLUS_DI()

ch.pri
ch.sec

qm.go_offline()
# qm.go_online()
fig = ch.to_figure()
fig
# print(fig)
# qm.go_online()
# ch.plot(title=False)
ch.plot(kind='candlestick', width=1650, volume=True)
