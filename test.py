
# In[]:
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
ch.op
#del ch.df['Open']
ch.df
ch.ind
ch.adjust(inplace=True)
ch.has_OHLC
print(ch.is_OHLC)
#ch.add_MA(50)
#ch.add_SMA(50)
#ch.add_EMA(200)
ch.add_BBANDS(30)
ch.ind
ch.plot()
