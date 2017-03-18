"""High-level functions meant for user access.

This includes various plotting and theming tools.

"""
from __future__ import absolute_import

import six
import copy

import auth
import utils
from theming.skeleton import SKELETON
from theming.themes import THEMES


_VALID_BASE_COMPONENTS = {'base_colors', 'base_traces',
                          'base_additions', 'base_layout'}

_VALID_THEME_COMPONENTS = {'colors', 'traces', 'additions', 'layout'}

_VALID_COLORS = {'increasing', 'decreasing', 'background',
                 'primary', 'secondary', 'tertiary'}

_VALID_TRACES = {'candlestick',
                 'line', 'line_thin', 'line_thick', 'line_dashed',
                 'line_dashed_thin', 'line_dashed_thick',
                 'area', 'area_dashed', 'area_threshold',
                 'scatter', 'bar', 'histogram'}

_VALID_ADDITIONS = {'xaxis', 'yaxis'}

_VALID_LAYOUT = {'font', 'plot_bgcolor', 'paper_bgcolor'}

# Common alternative spellings (from Matplotlib)
_VALID_TEMPLATE_KWARGS = {'xlabel', 'ylabel', 'xitle', 'ytitle',
                          'xTitle', 'yTitle', 'xrange', 'yrange',
                          'log', 'xlog', 'ylog', 'logx', 'logy'}

def get_theme(theme):
    """Return a Quantmod theme (as a dict).

    Parameters
    ----------
        theme : string
            Quantmod theme

    """
    if theme in THEMES:
        return copy.deepcopy(THEMES[theme])
    else:
        raise Exception("Invalid theme '{0}'.".format(theme))


def get_themes():
    """Return the list of available themes, or none if there is a problem."""
    return list(THEMES.keys())


def get_skeleton():
    """Return the base Quantmod skeleton."""
    return copy.deepcopy(SKELETON)


def make_colors(base_colors, colors):
    """Make trace configuration from theme/skeleton and theme/colors.

    Recursively update base_theme with theme using custom tool in utils.

    Parameters
    ----------
        base_colors : dict
            Additions file containing primitives from 'skeleton.py'.
        colors : dict
            Additions configuration from specified theme.

    """
    for key in colors.keys():
        if key not in _VALID_COLORS:
            raise Exception("Invalid keyword '{0}'".format(key))

    def _expand(base_colors):
        pass

    _expand(base_colors)

    # Modifiers directly to base_colors
    for key in colors.keys():
        utils.update(base_colors[key], colors[key])

    for key in base_colors.keys():
        if key not in _VALID_COLORS:
            raise Exception("Invalid keyword '{0}'".format(key))

    return base_colors


def make_traces(base_traces, traces):
    """Make trace configuration from theme/skeleton and theme/traces.

    Recursively update base_theme with theme using custom tool in utils.

    Parameters
    ----------
        base_traces : dict
            Trace file containing primitives from 'skeleton.py'.
        traces : dict
            Trace configuration from specified theme.

    """
    # Check for invalid entries
    for key in traces.keys():
        if key not in _VALID_TRACES:
            raise Exception("Invalid keyword '{0}'".format(key))

    def _expand(base_traces):
        """Creates other traces from the three elementary ones."""
        base_traces['candlestick']

        base_traces['line']
        base_traces['line_thin'] = copy.deepcopy(base_traces['line'])
        base_traces['line_thick'] = copy.deepcopy(base_traces['line'])
        base_traces['line_dashed'] = copy.deepcopy(base_traces['line'])
        base_traces['line_dashed_thin'] = copy.deepcopy(base_traces['line'])
        base_traces['line_dashed_thick'] = copy.deepcopy(base_traces['line'])

        base_traces['area'] = copy.deepcopy(base_traces['line'])
        base_traces['area']['fill'] = 'tonexty'
        base_traces['area_dashed'] = copy.deepcopy(base_traces['area'])
        base_traces['area_threshold'] = copy.deepcopy(base_traces['area'])

        base_traces['scatter'] = copy.deepcopy(base_traces['line'])
        base_traces['scatter']['mode'] = 'markers'

        base_traces['bar']
        base_traces['histogram'] = copy.deepcopy(base_traces['bar'])

    _expand(base_traces)

    # Mdifiers currently to 'line' only
    # This may be subject to laterchange
    for key in traces.keys():
        utils.update(base_traces[key]['line'], traces[key])

    # Check after copying
    for key in base_traces.keys():
        if key not in _VALID_TRACES:
            raise Exception("Invalid keyword '{0}'".format(key))

    return base_traces


def make_additions(base_additions, additions):
    """Make trace configuration from theme/skeleton and theme/additions.

    Recursively update base_theme with theme using custom tool in utils.

    Parameters
    ----------
        base_additions : dict
            Additions file containing primitives from 'skeleton.py'.
        additions : dict
            Additions configuration from specified theme.

    """
    for key in additions.keys():
        if key not in _VALID_ADDITIONS:
            raise Exception("Invalid keyword '{0}'".format(key))

    def _expand(base_additions):
        base_additions['xaxis']
        base_additions['yaxis']

    _expand(base_additions)

    # Modifiers directly to base_additions
    for key in additions.keys():
        utils.update(base_additions[key], additions[key])

    for key in base_additions.keys():
        if key not in _VALID_ADDITIONS:
            raise Exception("Invalid keyword '{0}'".format(key))

    return base_additions







def make_layout(base_traces, traces, **kwargs):

    for key in traces.keys():
        if key not in _VALID_LAYOUT:
            raise Exception("Invalid keyword '{0}'".format(key))








def make_template(theme=None, layout=None, legend=None, annotations=None,
                  title=None, xaxis_title=None, yaxis_title=None,
                  xaxis_log = None, yaxis_log = None,
                  xaxis_range = None, yaxis_range = None,
                  dimensions=None, height=None, width=None, margin=None,
                  **kwargs):
    """Generate color, traces, additions and layout dicts.

    Parameters
    ----------
        theme : string
            Quantmod theme
        layout : dict or graph_objs.Layout
            Plotly layout dict or graph_objs.Layout figure
        legend : dict
            BLABLA
        annotations : list
            BLABLA
        title : string
            BLABLALA
        xaxis_title : string
            BLABLA
        yaxis_title : string
            BLABLA
        xaxis_log : bool
            BLABLA
        yaxis_log : bool
            BLABLA
        dimensions : tuple
            BLABLA
        height : int
            BLABLA
        width : int
            BLABLA
        margin : dict or tuple
            BLABLA
    """
    # Check for kwargs integrity
    if kwargs:
        for key in kwargs.keys():
            if key not in _VALID_TEMPLATE_KWARGS:
                raise Exception("Invalid keyword '{0}'.".format(key))

        # Rename
        if 'xlabel' in kwargs:
            xaxis_title = kwargs['xlabel'] # Matplotlib
        if 'xtitle' in kwargs:
            xaxis_title = kwargs['xtitle'] # Cufflinks
        if 'xTitle' in kwargs:
            xaxis_title = kwargs['xTitle'] # Cufflinks

        if 'xlabel' in kwargs:
            xaxis_title = kwargs['xlabel'] # Matplotlib
        if 'xtitle' in kwargs:
            xaxis_title = kwargs['xtitle'] # Cufflinks
        if 'xTitle' in kwargs:
            xaxis_title = kwargs['xTitle'] # Cufflinks

        if 'xrange' in kwargs:
            xaxis_range = kwargs['xrange']
        if 'yrange' in kwargs:
            yaxis_range = kwargs['yrange']

        if 'log' in kwargs:
            yaxis_log = kwargs['log']

        if 'xlog' in kwargs:
            xaxis_log = kwargs['xlog']
        if 'logx' in kwargs:
            xaxis_log = kwargs['logx']

        if 'ylog' in kwargs:
            xaxis_log = kwargs['ylog']
        if 'logy' in kwargs:
            xaxis_log = kwargs['logy']

    # Coerce Layout() to regular dict
    if layout:
        if not isinstance(layout, dict):
            try:
                layout = dict(layout.items())
            except:
                raise Exception("Invalid layout '{0}'.".format(layout))

    # Get theme
    if not theme:
        theme = auth.get_config_file()['theme']
    if isinstance(theme, dict):
        theme = theme
    else:
        theme = get_theme(theme)

    # Get skeleton
    skeleton = get_skeleton()

    # Split theme and skeleton
    if all(key in skeleton.keys() for key in _VALID_BASE_COMPONENTS):
        base_colors = skeleton['base_colors']
        base_traces = skeleton['base_traces']
        base_additions = skeleton['base_additions']
        base_layout = skeleton['base_layout']
    else:
        raise Exception("Improperly configured skeleton. \
                        Consider reinstalling Quantmod.")

    if all(key in theme.keys() for key in _VALID_THEME_COMPONENTS):
        colors = theme['colors']
        traces = theme['traces']
        additions = theme['additions']
        layout = theme['layout']
    else:
        raise Exception("Improperly configured theme '{0}'.".format(theme))

    # Generate final template
    colors = make_colors(base_colors, colors)
    traces = make_traces(base_traces, traces)
    additions = make_additions(base_additions, additions)
    layout = make_layout(base_layout, layout, legend, annotations,
                         title, xaxis_title, yaxis_title,
                         xaxis_log, yaxis_log, xaxis_range, yaxis_range,
                         dimensions, height, width, margin, **kwargs)

    # Convert to dict
    template = dict(colors=colors, traces=traces,
                    additions=additions, layout=layout)

    return template
