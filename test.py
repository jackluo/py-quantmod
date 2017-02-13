import quantmod.chart as qm
from quantmod.themes.themes import base_template, get_light_theme
import pandas as pd
import pandas_datareader as web


# In[]:
ticker = 'AAPL'

template, layout = get_light_theme()

df = web.DataReader(ticker, data_source='yahoo')
ch = qm.Chart(df)
ch = ch.adjust()
#ch.MA(50)
#ch.SMA(50)
#ch.EMA(200)
ch.plot()
