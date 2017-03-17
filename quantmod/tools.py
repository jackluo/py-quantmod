"""High-level functions not meant for user access.

This includes various plotting and theming tools.

"""
from __future__ import absolute_import

import copy
#from plotly.graph_objs import *
import auth
from theming.skeleton import SKELETON
from theming.themes import THEMES


_TEMPLATE_KWARGS = ['legend', 'vline', 'hline', 'vspan', 'hspan', 'shapes', 'logx', 'logy',
                   'xrange', 'yrange', 'zrange']

def get_theme(theme):
    """Return a Quantmod theme (as a dict)."""
    if theme in THEMES:
        return copy.deepcopy(THEMES[theme])
    else:
        raise Exception("Invalid theme '{0}'".format(theme))


def get_themes():
    """Return the list of available themes."""
    return list(THEMES.keys())


def get_skeleton():
    """Return base template."""
    return copy.deepcopy(SKELETON)


def make_template(theme=None, layout=None, **kwargs):
    """Generate a colors, traces, additions and layout

    Parameters
    ----------
            theme : string
                Quantmod theme
            layout : dict or graph_objs.Layout
                Plotly layout dict or graph_objs.Layout figure

    """
    for key in kwargs.keys():
        if key not in _TEMPLATE_KWARGS:
            raise Exception("Invalid keyword '{0}'".format(key))

    if not theme:
        theme = auth.get_config_file()['theme']

    if layout:
        if not isinstance(layout, dict):
            try:
                layout = dict(layout.items()) # Coerce to regular dict
            except:
                raise Exception("Invalid layout '{0}'".format(layout))


    template = get_template()
    colors, traces, additions, layout = template['base_colors'], template['base_traces'],
                                        template['base_additions'], template['base_layout']

    theme = get_theme(theme)


    def get_colors(theme=None):

        if not theme:
            theme = auth.get_config_file()['theme']

        colors = get_theme(theme)['colors']
        return colors

    def get_traces(theme=None):

        if not theme:
            theme = auth.get_config_file()['theme']

        base_traces = get_template()
        traces = get_theme(theme)['traces']
        deep_update(base_traces, traces)

        return base_traces


    def get_additions(theme=None):

        if not theme:
            theme = auth.get_config_file()['theme']

        base_additions = get_template()['base_additions']
        additions = get(theme)['additions']
        deep_update(base_additions, additions)

        return base_additions


    def get_layout(theme=None, layout=None, **kwargs):
        """Generate a Plotly layout

        Parameters
        ----------
                theme : string
                    Quantmod theme
                layout : dict or graph_objs.Layout
                    Plotly layout dict or graph_objs.Layout figure

        """
        for key in kwargs.keys():
            if key not in __LAYOUT_KWARGS:
                raise Exception("Invalid keyword '{0}'".format(key))

        if not theme:
            theme = auth.get_config_file()['theme']

        if layout:
            if not isinstance(layout, dict):
                try:
                    layout = dict(layout.items()) # Coerce to regular dict
                except:
                    raise Exception("Invalid layout '{0}'".format(layout))



get_layout()


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


def merge_dict(dict1, dict2):
    """Merge 2 Python dicts (shallow copy)."""
    dct = dict1.copy()
    return dct.update(dict2)


def deep_update(dict1, dict2):
    """Updates the values (deep form) of a given dictionary.

    Parameters
    ----------
            dict1 : dict
                    Dictionary that contains the values to update.
            dict2 : dict
                    Dictionary to be updated.

    """
    for key, value in dict2.items():
        if isinstance(value, dict):
            if key in dict1:
                deep_update(dict1[key], value)
            else:
                dict1[key] = value
        else:
            dict1[key] = value

    return dict1
