"""Quantmod

A Python port of R's famous Quantmod library.
Based on Plotly and Cufflinks, Quantmod provides pretty charting
and a variety of quant and technical finance tools.

Contrib
-------
author : @jackwluo
cufflinks: @jorgesantos

"""

from .plotlytools import *
from .ta import *
from .version import __version__

"""
#from . import date_tools
#from . import utils
#from . import datagen
#from . import tools
#from . import colors
#from . import pandastools
from .utils import pp
from .tools import subplots, scatter_matrix, figures, getLayout, getThemes, getTheme
from .extract import to_df
from .auth import set_config_file, get_config_file
from .offline import is_offline, go_offline, go_online

try:
    if get_config_file()['offline']:
        go_offline()
    else:
        go_online()
except:
    pass
"""
