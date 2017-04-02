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
# flake8: noqa

from __future__ import absolute_import


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


from .core import *
from .chart import *
from .tools import (go_offline, go_online, is_offline,
                    get_config_file, set_config_file, reset_config_file,
                    get_credentials_file, set_credentials_file,
                    reset_credentials_file)
from .version import __version__

# Offline mode from config initialization
try:
	if get_config_file()['offline']:
		go_offline()
	else:
		go_online()
except:
	pass
