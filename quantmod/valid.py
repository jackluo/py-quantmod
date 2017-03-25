"""Function validity module not meant for user access

Quantmod functions have checks against these sets below to guard
against bad input.

"""
# Mandatory dict names for skeleton structure
VALID_BASE_COMPONENTS = {'base_colors', 'base_traces',
                         'base_additions', 'base_layout',}

# Mandatory dict names for theme structure
VALID_THEME_COMPONENTS = {'colors', 'traces', 'additions', 'layout',}

# Valid colors for base_colors or colors
VALID_COLORS = {'increasing', 'decreasing', 'border',
                'primary', 'secondary', 'tertiary',
                'grey', 'grey_light', 'grey_strong',
                'fill', 'fill_light', 'fill_strong',
                'fillcolor',}

# Valid trace types for base_traces or traces
VALID_TRACES = {'ohlc', 'candlestick',
                'line', 'line_thin', 'line_thick', 'line_dashed',
                'line_dashed_thin', 'line_dashed_thick',
                'area', 'area_dashed',
                'area_dashed_thin', 'area_dashed_thick', 'area_threshold',
                'scatter', 'bar', 'histogram',}

OHLC_TRACES = {'ohlc', 'candlestick'}

OTHER_TRACES = VALID_TRACES - OHLC_TRACES

# Valid addition types for baes_additions or additions
VALID_ADDITIONS = {'xaxis', 'yaxis',}

# Valid layout arguements for base_layout or layout
VALID_LAYOUT = {'title', 'width', 'height', 'autosize',
                'font', 'margin', 'hovermode', 'barmode',
                'bargap', 'bargroupgap', 'boxgap', 'boxgroupgap',
                'plot_bgcolor', 'paper_bgcolor',
                'showlegend', 'legend',}

# Valid columns for Chart
VALID_COLUMNS = {'op', 'hi', 'lo', 'cl',
                 'aop', 'ahi', 'alo', 'acl',
                 'vo', 'di',}

# Alternative syntax for get_template and make_layout
VALID_TEMPLATE_KWARGS = {'showlegend', 'figsize',}

# Alternative syntax for to_frame
VALID_FIGURE_KWARGS = {'kind', 'subtitles', 'showlegend', 'figsize',}
