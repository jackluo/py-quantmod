"""Functions that manage online/offline plotting.

Based on Cufflinks' offline.py.

"""
import plotly.offline as pyo
from auth import get_config_file


def go_offline(connected=False):
    """Take plotting offline."""
    pyo.init_notebook_mode(connected)
    pyo.__PLOTLY_OFFLINE_INITIALIZED = True


def go_online():
    """Take plotting offline."""
    pyo.__PLOTLY_OFFLINE_INITIALIZED = False


def is_offline():
    """Check on/offline status."""
    return pyo.__PLOTLY_OFFLINE_INITIALIZED


go_offline()
print(is_offline())
