# In[]:

import numpy as np
import quantmod as qm
import pandas as pd
import pandas_datareader as web


# In[]:

ticker = 'AAPL'
df = web.DataReader(ticker, data_source='yahoo')
df = df.head(365)
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

ch.add_MA(type='line_dashed')
ch.add_SMA(type='line_dashed')
ch.add_EMA(type='line_dashed')
ch.add_WMA(type='line_dashed')
ch.add_DEMA(type='line_dashed')
ch.add_TEMA(type='line_dashed')
ch.add_T3(type='line_dashed')
ch.add_KAMA(type='line_dashed')
ch.add_TRIMA(type='line_dashed')
ch.add_MAMA(type='line_dashed')
# ch.add_MAVP(type='line_dashed')
ch.add_MIDPOINT(type='line_dashed')
ch.add_BBANDS(type='line_dashed')
ch.add_SAR(type='line_dashed')
ch.add_SAREXT(type='line_dashed')
ch.add_HT_TRENDLINE(type='line_dashed')
# ch.add_RSI(type='line_dashed')
ch.add_ADX(type='line_dashed')

qm.go_offline()
qm.go_online()
ch.to_figure()
# qm.go_online()
# ch.plot(title=False)
ch.plot(kind='candlestick', margin=dict(t=10, b=10, r=10, l=40), volume=True)
