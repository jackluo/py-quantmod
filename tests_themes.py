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
ch.add_T3()
ch.plot(kind='candlestick', theme='light', volume=True)
ch.plot(kind='candlestick', theme='dark', volume=True)
ch.ind.tail(100)
