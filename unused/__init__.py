# From pandas/__init__.py

# pylint: disable-msg=W0614,W0401,W0611,W0622
# flake8: noqa

__docformat__ = 'restructuredtext'

hard_dependencies = ('numpy',
                     'pandas',
                     'plotly',
                     'pandas_datareader')
missing_dependencies = []

for dependency in hard_dependencies:
    try:
        __import__(dependency)
    except ImportError as e:
        missing_dependencies.append(dependency)

if missing_dependencies:
    raise ImportError(
        "Missing required dependencies {0}.".format(missing_dependencies))
del hard_dependencies, dependency, missing_dependencies

from core import *
from chart import *
from offline import is_offline, go_ofline, go_online
from version import __version__

import stylesheets

try:
	if get_config_file()['offline']:
		go_offline()
	else:
		go_online()
except:
	pass

"""
from . import date_tools
from . import utils
from . import datagen
from . import tools
from . import colors
from . import pandastools
from . import ta

from .plotlytools import *
from plotly.plotly import plot
from .colors import cnames, get_colorscale
from .utils import pp
from .tools import subplots,scatter_matrix,figures,getLayout,getThemes,getTheme
from .extract import to_df
from .auth import set_config_file,get_config_file
from .offline import is_offline,go_offline,go_online
from .version import __version__

try:
	if get_config_file()['offline']:
		go_offline()
	else:
		go_online()
except:
	pass
"""
