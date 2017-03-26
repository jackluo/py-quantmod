"""Functions that manage online/offline plotting

Refactored from Cufflinks' 'offline.py' module.

"""
from __future__ import absolute_import

import plotly.offline as pyo


def go_offline(connected=False):
    """Take plotting offline.

    __PLOTLY_OFFLINE_INITIALIZED is a secret variable
    in plotly/offline/offline.py.

    """
    try:
        pyo.init_notebook_mode(connected)
    except TypeError:
        pyo.init_notebook_mode()

    pyo.__PLOTLY_OFFLINE_INITIALIZED=True


def go_online():
    """Take plotting offline."""
    pyo.__PLOTLY_OFFLINE_INITIALIZED = False


def is_offline():
    """Check online/offline status."""
    return pyo.__PLOTLY_OFFLINE_INITIALIZED
