"""High-level functions meant for user access

This includes various plotting and theming helpers.
Module also contains all argument validity checks.

"""
from __future__ import absolute_import

import six
import copy

from . import utils
from . import tools
from .theming.skeleton import SKELETON
from .theming.themes import THEMES
from .vendors.sources import SOURCES
from .valid import (VALID_COLORS, VALID_TRACES,
                    VALID_LAYOUT, VALID_ADDITIONS,
                    VALID_TEMPLATE_KWARGS,
                    VALID_BASE_COMPONENTS,
                    VALID_THEME_COMPONENTS)


def get_theme(theme):
    """Return a Quantmod theme (as a dict).

    Parameters
    ----------
        theme : string
            Quantmod theme.

    """
    if theme in THEMES:
        return copy.deepcopy(THEMES[theme])
    else:
        raise Exception("Theme not found '{0}'.".format(theme))


def get_themes():
    """Return the list of available themes, or none if there is a problem."""
    return list(THEMES)


def get_skeleton():
    """Return the base Quantmod skeleton."""
    return copy.deepcopy(SKELETON)


def get_source(source):
    """Return a Quantmod source (as a dict).

    Parameters
    ----------
        source : string
            Quantmod source.

    """
    if source in SOURCES:
        return copy.deepcopy(SOURCES[source])
    else:
        raise Exception("Source not found '{0}'.".format(source))


def get_sources():
    """Return the list of available sources, or none if there is a problem."""
    return list(SOURCES)


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
    for key in colors:
        if key not in VALID_COLORS:
            raise Exception("Invalid keyword '{0}'".format(key))

    def _expand(base_colors):
        pass

    _expand(base_colors)

    # Modifiers directly to base_colors
    utils.update(base_colors, colors)

    for key in base_colors:
        if key not in VALID_COLORS:
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
    for key in traces:
        if key not in VALID_TRACES:
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
        base_traces['area_dashed_thin'] = copy.deepcopy(base_traces['area'])
        base_traces['area_dashed_thick'] = copy.deepcopy(base_traces['area'])
        base_traces['area_threshold'] = copy.deepcopy(base_traces['area'])

        base_traces['scatter'] = copy.deepcopy(base_traces['line'])
        base_traces['scatter']['mode'] = 'markers'
        base_traces['scatter']['opacity'] = 1.0

        base_traces['bar']
        base_traces['histogram'] = copy.deepcopy(base_traces['bar'])

    _expand(base_traces)

    # Mdifiers currently to 'line' only
    # This may be subject to laterchange
    for key in traces:
        utils.update(base_traces[key]['line'], traces[key])

    # Check after copying
    for key in base_traces:
        if key not in VALID_TRACES:
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
    for key in additions:
        if key not in VALID_ADDITIONS:
            raise Exception("Invalid keyword '{0}'".format(key))

    # No utility right now, planned in the future for additions
    def _expand(base_additions):
        pass

    _expand(base_additions)

    # Modifiers directly to base_additions
    utils.update(base_additions, additions)

    for key in base_additions:
        if key not in VALID_ADDITIONS:
            raise Exception("Invalid keyword '{0}'".format(key))

    return base_additions


def make_layout(base_layout, layout, custom_layout,
                title, hovermode,
                legend, annotations, shapes,
                dimensions, width, height, margin, **kwargs):
    """Make layout configuration from theme/skeleton and theme/traces.

    Recursively update base_theme with theme using custom tool in utils.

    Parameters
    ----------
        base_traces : dict
            Layout file containing primitives from 'skeleton.py'.
        layout : dict
            Layout configuration from specified theme.
        custom_layout : dict
            Plotly layout dict or graph_objs.Layout object.
            Will override all other arguments if conflicting as
            user-inputted layout is updated last.
        title : string
            Chart title.
        hovermode : {'x', 'y', 'closest', False}
            Toggle how a tooltip appears on cursor hover.
        legend : dict, Legend or bool
            True/False or Plotly legend dict / graph_objs.Legend object.
            If legend is bool, Quantmod will only toggle legend visibility.
        annotations : list
            Plotly annotations list.
        shapes : list or
            Plotly shapes list.
        dimensions : tuple
            Dimensions 2-tuple in order (width, height).
            Disables autosize=True.
        width : int
            Width of chart. Default 1080 pixels.
            If used with height, disables autosize=True (Equivalent to
            using dimensions).
        height : int
            Height of chart. Default 720 pixels.
            If used with width, disables autosize=True (Equivalent to
            using dimensions).
        margin : dict or tuple
            Plotly margin dict or 4-tuple in order (l, r, b, t) or
            5-tuple in order (l, r, b, t, margin). Tuple input added for
            Cufflinks compatibility.

    """
    # Check for kwargs integrity
    for key in kwargs:
        if key not in VALID_TEMPLATE_KWARGS:
            raise Exception("Invalid keyword '{0}'.".format(key))

    # Kwargs
    if 'showlegend' in kwargs:
        legend = kwargs['showlegend']

    if 'figsize' in kwargs:  # Matplotlib
        figsize = kwargs['figsize']
        if isinstance(figsize, tuple):
            if len(figsize) == 2:
                dimensions = tuple(80 * i for i in figsize)  # 80x size
            else:
                raise Exception("Invalid figsize '{0}'. "
                                "It should be tuple of len 2."
                                .format(figsize))
        else:
            raise TypeError("Invalid figsize '{0}'. "
                            "It should be tuple."
                            .format(figsize))

    # Check for invalid entries
    for key in layout:
        if key not in VALID_LAYOUT:
            raise Exception("Invalid keyword '{0}'".format(key))

    # No utility right now, planned in the future for additions
    def _expand(base_layout):
        pass

    _expand(base_layout)

    # Modifiers directly to base_layout
    utils.update(base_layout, layout)

    if title is not None:
        base_layout['title'] = title

    if hovermode is not None:
        base_layout['hovermode'] = hovermode

    if legend is not None:
        if legend is True:
            base_layout['showlegend'] = True
        elif legend is False:
            base_layout['showlegend'] = False
        else:
            base_layout['showlegend'] = True
            base_layout['legend'] = legend

    if annotations is not None:
        base_layout['annotations'] = annotations

    if shapes is not None:
        base_layout['shapes'] = shapes

    if dimensions is not None:
        base_layout['width'] = dimensions[0]
        base_layout['height'] = dimensions[1]
        base_layout['autosize'] = False

    if width is not None:
        base_layout['width'] = width

    if height is not None:
        base_layout['height'] = height

    if width is not None and height is not None:
        base_layout['autosize'] = False

    if margin is not None:
        base_layout['margin'] = margin

    # Custom layout update
    if custom_layout is not None:
        utils.update(layout, custom_layout)

    for key in base_layout:
        if key not in VALID_LAYOUT:
            raise Exception("Invalid keyword '{0}'".format(key))

    return base_layout


def get_template(theme=None, layout=None,
                 title=None, hovermode=None,
                 legend=None, annotations=None, shapes=None,
                 dimensions=None, width=None, height=None, margin=None,
                 **kwargs):
    """Generate color, traces, additions and layout dicts.

    Parameters
    ----------
        theme : string
            Quantmod theme.
        layout : dict or Layout
            Plotly layout dict or graph_objs.Layout object.
            Will override all other arguments if conflicting as
            user-inputted layout is updated last.
        title : string
            Chart title.
        hovermode : {'x', 'y', 'closest', False}
            Toggle how a tooltip appears on cursor hover.
        legend : dict, Legend or bool
            True/False or Plotly legend dict / graph_objs.Legend object.
            If legend is bool, Quantmod will only toggle legend visibility.
        annotations : list or Annotations
            Plotly annotations list / graph.objs.Annotations object.
        shapes : list or Shapes
            Plotly shapes list or graph_objs.Shapes object.
        dimensions : tuple
            Dimensions 2-tuple in order (width, height).
            Disables autosize=True.
        width : int
            Width of chart. Default 1080 pixels.
            If used with height, disables autosize=True (Equivalent to
            using dimensions).
        height : int
            Height of chart. Default 720 pixels.
            If used with width, disables autosize=True (Equivalent to
            using dimensions).
        margin : dict or tuple
            Plotly margin dict or 4-tuple in order (l, r, b, t) or
            5-tuple in order (l, r, b, t, margin). Tuple input added for
            Cufflinks compatibility.

    """
    # Check for kwargs integrity
    for key in kwargs:
        if key not in VALID_TEMPLATE_KWARGS:
            raise Exception("Invalid keyword '{0}'.".format(key))

    # Kwargs renaming
    if 'showlegend' in kwargs:
        legend = kwargs['showlegend']

    if 'figsize' in kwargs:  # Matplotlib
        figsize = kwargs['figsize']
        if isinstance(figsize, tuple):
            if len(figsize) == 2:
                dimensions = tuple(80 * i for i in figsize)  # 80x size
            else:
                raise Exception("Invalid figsize '{0}'. "
                                "It should be tuple of len 2."
                                .format(figsize))
        else:
            raise TypeError("Invalid figsize '{0}'. "
                            "It should be tuple."
                            .format(figsize))

    # Get skeleton
    skeleton = get_skeleton()

    # Type checks for optionally used arguments

    # The if x not None: pattern is used instead of if x:
    # because it can catch other falsey values like False,
    # which may cause side effects to Plotly.py.

    # Test if theme is string or dict, get default theme from config otherwise
    if theme is not None:
        if isinstance(theme, six.string_types):
            theme = get_theme(theme)
        elif isinstance(theme, dict):
            pass
        else:
            raise TypeError("Invalid theme '{0}'. "
                            "It should be string or dict."
                            .format(theme))
    else:
        theme = get_theme(tools.get_config_file()['theme'])

    # Test if layout is dict, else coerce Layout to regular dict
    # Rename to custom_layout (to distinguish from base_layout and layout)
    if layout is not None:
        custom_layout = layout
        if not isinstance(custom_layout, dict):
            try:
                custom_layout = dict(custom_layout.items())
            except:
                raise TypeError("Invalid layout '{0}'. "
                                "It should be dict or graph_objs.Layout."
                                .format(custom_layout))
    else:
        custom_layout = None

    # Test title if string, else raise exception
    if title is not None:
        if not isinstance(title, six.string_types):
            raise TypeError("Invalid title '{0}'. "
                            "It should be string.".format(title))

    # Test if hovermode is string or False, else raise exception
    if hovermode is not None:
        if hovermode is False:
            pass
        elif isinstance(hovermode, six.string_types):
            pass
        else:
            raise TypeError("Invalid hovermode '{0}'. "
                            "It should be string or 'False'."
                            .format(hovermode))

    # Test if legend is True/False, else coerce Legend to regular dict
    # if legend is not regular dict
    if legend is not None:
        if isinstance(legend, bool):
            pass
        elif isinstance(legend, dict):
            pass
        else:
            try:
                layout = dict(layout.items())
            except:
                raise TypeError("Invalid legend '{0}'. "
                                "It should be bool, dict or graph_objs.Legend."
                                .format(layout))

    # Test if annotations is list, else coerce Annotations to regular list
    if annotations is not None:
        if not isinstance(annotations, list):
            try:
                annotations = list(annotations)
            except:
                raise TypeError("Invalid annotations '{0}'. "
                                "It should be list or graph_objs.Annotations."
                                .format(annotations))

    # Test is shapes is list, else coerce Shapes into regular list
    if shapes is not None:
        if not isinstance(shapes, list):
            try:
                shapes = list(shapes)
            except:
                raise TypeError("Invalid shapes '{0}'. "
                                "It should be list or graph_objs.Shapes."
                                .format(shapes))

    # Test if dimensions is tuple, else raise exception
    if dimensions is not None:  # Cufflinks
        if not isinstance(dimensions, tuple):
            raise TypeError("Invalid dimensions '{0}'. "
                            "It should be tuple."
                            .format(dimensions))
            if not len(dimensions) == 2:
                raise Exception("Invalid dimensions '{0}'. "
                                "It should be tuple of len 2."
                                .format(dimensions))

    # Test below items if int, else raise exception
    if width is not None:
        if not isinstance(width, six.integer_types):
            raise TypeError("Invalid width '{0}'. "
                            "It should be int."
                            .format(width))

    if height is not None:
        if not isinstance(height, six.integer_types):
            raise TypeError("Invalid height '{0}'. "
                            "It should be int."
                            .format(height))

    # Test if margin is dict, else convert tuple to dict, else raise exception
    if margin is not None:
        if isinstance(margin, dict):
            pass
        elif isinstance(margin, tuple):  # Cufflinks
            if len(margin) == 4:
                margin = dict(zip(('l', 'r', 'b', 't'), margin))
            elif len(margin) == 5:
                margin = dict(zip(('l', 'r', 'b', 't', 'pad'), margin))
            else:
                raise Exception("Invalid margin '{0}'. "
                                "It should be tuple of len 4 or 5."
                                .format(margin))
        else:
            raise TypeError("Invalid margin '{0}'. "
                            "It should be dict or tuple."
                            .format(margin))

    # Split theme and skeleton
    if all(key in skeleton for key in VALID_BASE_COMPONENTS):
        base_colors = skeleton['base_colors']
        base_traces = skeleton['base_traces']
        base_additions = skeleton['base_additions']
        base_layout = skeleton['base_layout']
    else:
        raise Exception("Improperly configured skeleton. "
                        "Consider reinstalling Quantmod.")

    if all(key in theme for key in VALID_THEME_COMPONENTS):
        colors = theme['colors']
        traces = theme['traces']
        additions = theme['additions']
        layout = theme['layout']
    else:
        raise Exception("Improperly configured theme '{0}'.".format(theme))

    # Generate final template
    final_colors = make_colors(base_colors, colors)
    final_traces = make_traces(base_traces, traces)
    final_additions = make_additions(base_additions, additions)
    final_layout = make_layout(base_layout, layout, custom_layout,
                               title, hovermode,
                               legend, annotations, shapes,
                               dimensions, width, height, margin)

    # Convert to dict
    template = dict(colors=final_colors, traces=final_traces,
                    additions=final_additions, layout=final_layout)

    return template


def get_base_layout(figures):
    """Generate a layout with the union of multiple figures' layouts.

    Parameters
    ----------
        figures : list
            List of Plotly figures to get base layout from.

    """
    if not isinstance(figures, list):
        raise TypeError("Invalid figures '{0}'. "
                        "It should be list."
                        .format(figures))

    layout = {}
    for figure in figures:
        if not figure['layout']:
            raise Exception("Figure does not have 'layout'.")

        for key, value in figure['layout'].items():
            layout[key] = value

    return layout


def strip_figure(figure):
    """Strip a Plotly figure into multiple figures with a trace on each of them.

    Parameters
    ----------
        figure : dict or Figure
            Plotly figure to strip into multiple figures.

    """
    if figure is not None:
        if isinstance(figure, dict):
            pass
        else:
            try:
                figure = dict(figure.items())
            except:
                raise TypeError("Invalid figure '{0}'. "
                                "It should be dict or graph_objs.Legend."
                                .format(figure))

    if not figure['layout']:
        raise Exception("Figure does not have 'data'.")

    figures = []
    for trace in figure['data']:
        figures.append(dict(data=[trace], layout=figure['layout']))

    return figures
