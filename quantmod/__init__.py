"""Quantmod

A powerful financial charting library based on R's Quantmod.

With a Plotly backend and Cufflinks simplicity,
Quantmod provides beautiful charts and a variety of
quantitiative and technical finance tools.

Author
------
    @jackwluo

Credits
-------
    plotly.py : @chriddyp, @theengineear, et al.
    cufflinks : @jorgesantos

"""
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


from __future__ import absolute_import


from .core import *
from .chart import *
from .auth import get_config_file, set_config_file
from .offline import go_offline, go_online
from .version import __version__

# Offline mode from config initialization
try:
	if get_config_file()['offline']:
		go_offline()
	else:
		go_online()
except:
	pass
