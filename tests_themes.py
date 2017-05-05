# In[]:

import numpy as np
import quantmod as qm
import pandas as pd
import pandas_datareader as web


# In[]:

ch = qm.get_symbol('TSLA')

ch.adjust(inplace=True)
ch.add_RSI()
ch.add_MACD()
ch.add_EMA()
ch.add_BBANDS()
ch.plot(kind='candlestick', theme='light', log=True, volume=True)
ch.plot(kind='candlestick', theme='dark', log=True, volume=True)
ch.ind.tail(100)
