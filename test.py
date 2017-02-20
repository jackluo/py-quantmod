import quantmod.chart as qm
from quantmod.themes.themes import base_template, get_light_theme
import pandas as pd
import pandas_datareader as web


# In[]:
ticker = 'AAPL'

template, layout = get_light_theme()

df = web.DataReader(ticker, data_source='yahoo')
ch = qm.Chart(df)
ch.has_close
#ch.to_frame()
#del df['Close']
#del df['Adj Close']
ch.has_open
ch.has_close
ch.has_adjusted_close
ch.is_OHLC
#ch.MA(50)
#ch.SMA(50)
#ch.EMA(200)
ch.plot()

'a' in 'def'
'1' in '123'
