import copy

import auth
#from auth import default_theme
from themes import THEMES


__LAYOUT_KWARGS = ['legend', 'vline', 'hline', 'vspan', 'hspan', 'shapes', 'logx', 'logy', 'layout_update',
                   'xrange', 'yrange', 'zrange']

default_theme = 'light-qm'

def get_theme(theme):
    """Return a Quantmod theme (as a dict)."""
    if theme in THEMES:
        return copy.deepcopy(THEMES[theme])
    else:
        raise Exception('Invalid theme "{0}'.format(theme))


def get_themes():
    """Return the list of available themes."""
    return list(THEMES.keys())

def get_layout(theme=default_theme, **kwargs):
    """Generate a Plotly layout"""

    for key in kwargs.keys():
        if key not in __LAYOUT_KWARGS:
            raise Exception('Invalid keyword "{}"'.format(key))

    if not theme:
        theme = auth.get_config()['theme']

get_layout(legesdnd = "BB")



def merge_dict(dict1, dict2):
    """Merge 2 Python dicts (shallow copy)."""
    dct = dict1.copy()
    return dct.update(dict2)


def strip_figure(figure):
    """Strip a Plotly figure into multiple figures with a trace on each of them.

    Parameters
    ----------
    figure : dict or Figure()
        Plotly figure

    """
    figures = []
    for trace in figure['data']:
        figures.append(dict(data=[trace], layout=figure['layout']))
    return figures


def get_base_layout(figures):
    """Generate a layout with the union of all properties of multiple figures' layouts.

    Parameters
    ----------
    figures : list(dict or Figure())
        List of Plotly figures

    """
    layout = {}
    for figure in figures:
        for key, value in list(figure['layout'].items()):
            layout[key] = value
    return layout



def go_offline(connected=False, offline=True):
    if offline:
        py_offline.init_notebook_mode(connected)
        py_offline.__PLOTLY_OFFLINE_INITIALIZED = True
    else:
        py_offline.__PLOTLY_OFFLINE_INITIALIZED = False


def is_offline():
    return py_offline.__PLOTLY_OFFLINE_INITIALIZED
