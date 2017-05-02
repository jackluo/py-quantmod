# In[]:

import numpy as np
import quantmod as qm
import pandas as pd
import pandas_datareader as web


# In[]:

ticker = 'AAPL'
df = web.DataReader(ticker, data_source='yahoo', start='2016/01/01')
df = df.tail(365)
ch = qm.Chart(df, start='2015/01/01', end='2017/03/02')

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

ch.add_APO()
ch.add_AROON()
ch.add_AROONOSC()
ch.add_BOP()
ch.add_CCI()
ch.add_CMO()
ch.add_ADX()
ch.add_ADXR()
ch.add_DX()
ch.add_MINUS_DI()
ch.add_PLUS_DI()
ch.add_MINUS_DM()
ch.add_PLUS_DM()
ch.add_MACD()
ch.add_MACDEXT()
ch.add_MFI()
ch.add_MOM()
ch.add_PPO()
ch.add_ROC()
ch.add_ROCP()
ch.add_ROCR()
ch.add_ROCR100()
ch.add_RSI()
ch.add_STOCH()
ch.add_STOCHF()
ch.add_STOCHRSI()
ch.add_TRIX()
ch.add_ULTOSC()
ch.add_WILLR()

ch.plot(kind='candlestick', volume=True,
        title='Full Test', filename='full_test')


import quantmod as qm
ch = qm.get_symbol('QQQ', start='01/01/2016')
ch.add_EMA(9)
ch.add_RSI(14)
ch.iplot()
