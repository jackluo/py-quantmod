"""Quantmod skeleton module

Edit your own modules by copying one of the themes.
Make sure that colors, traces, additions and layout are all under one dict.

For readability, files under theming do not follow PEP8 guideline of
no space between assignment of named arguments.

"""
# flake8: noqa

_PLACEHOLDER = False

# Color primitives
BASE_COLORS = dict()

# Trace primitives
BASE_TRACES = dict(

    candlestick = dict(
        type = 'candlestick',
        hoverinfo = 'x+y+text+name',
        whiskerwidth = 0,
        # Increasing
        increasing = dict(
            line = dict(
                color = _PLACEHOLDER,
                width = 1,
            ),
            fillcolor = _PLACEHOLDER,
        ),
        # Decreasing
        decreasing = dict(
            line = dict(
                color = _PLACEHOLDER,
                width = 1,
            ),
            fillcolor = _PLACEHOLDER,
        ),
    ),

    ohlc = dict(
        type = 'ohlc',
        hoverinfo = 'x+y+text+name',
        # Increasing
        increasing = dict(
            line = dict(
                color = _PLACEHOLDER,
                width = 1.5,
            ),
        ),
        # Decreasing
        decreasing = dict(
            line = dict(
                color = _PLACEHOLDER,
                width = 1.5,
            ),
        ),
    ),

    line = dict(
        type = 'scatter',
        hoverinfo = 'x+y+text+name',
        mode = 'lines',
        #fill = 'tonexty',
        opacity = 0.6,
        # Marker
        marker = dict(
            color = _PLACEHOLDER,
            size = 3,
            opacity = 1.0,
            symbol = 'square',
        ),
        # Line
        line = dict(
            color = _PLACEHOLDER,
            width = 2,
            #dash = 4,
            #shape = 'spline',
            #smoothing = '2',
        ),
        # Area
        fillcolor = _PLACEHOLDER,
    ),

    bar = dict(
        type = 'bar',
        hoverinfo = 'x+y+text+name',
        #opacity = 0.6,
        # Marker
        marker = dict(
            color = _PLACEHOLDER,
            line = dict(
                color = _PLACEHOLDER,
                width = 1,
            ),
        ),
    ),

)

# Layout modifiers
BASE_ADDITIONS = dict(

    xaxis = dict(
        # Range
        #nticks = , #OR
        #tick0 = , #AND
        #dtick = ,
        # Ticks
        #tickfont = dict(size = 10),
        #showticklabels = False,
        # Range slider
        rangeslider = dict(
            visible = False,
            bordercolor = _PLACEHOLDER,
            bgcolor = _PLACEHOLDER,
            thickness = 0.1,
        ),
        # Range selector
        rangeselector = dict(
            visible = True,
            bordercolor = _PLACEHOLDER,
            bgcolor = _PLACEHOLDER,
            activecolor = _PLACEHOLDER,
            buttons = [
                dict(count = 1, step = 'day', stepmode = 'backward', label = '1D'),
                dict(count = 5, step = 'day', stepmode = 'backward', label = '5D'),
                dict(count = 1, step = 'month', stepmode = 'backward', label = '1M'),
                dict(count = 3, step = 'month', stepmode = 'backward', label = '3M'),
                dict(count = 6, step = 'month', stepmode = 'backward', label = '6M'),
                dict(count = 1, step = 'year', stepmode = 'backward', label = '1Y'),
                dict(count = 2, step = 'year', stepmode = 'backward', label = '2Y'),
                dict(count = 5, step = 'year', stepmode = 'backward', label = '5Y'),
                dict(count = 1, step = 'all', stepmode = 'backward', label = 'MAX'),
                dict(count = 1, step = 'year', stepmode = 'todate', label = 'YTD'),
            ],
        ),
        # Other
        #type = 'datetime'
        anchor = 'y',
        side = 'bottom',
        #showline = False,
        #showgrid = False,
        #zeroline = False,
        #titlefont = dict(size = 10),
    ),

    yaxis = dict(
        # Range
        #rangemode = 'tozero',
        #range = ,
        #nticks = , #OR
        #tick0 = , #AND
        #dtick = ,
        # Ticks
        #tickfont = dict(size = 10),
        #showticklabels = False,
        # Other
        type = 'linear',
        domain = [0.0, 1],
        side = 'right',
        #showline = False,
        #showgrid = False,
        #zeroline = False,
        #titlefont = dict(size = 10),
    ),

)

# Layout primitives
BASE_LAYOUT = dict(
    # General
    title = '',
    width = 1080,
    height = 720,
    autosize = True,
    font = dict(
        family = _PLACEHOLDER,
        size = _PLACEHOLDER,
        color = _PLACEHOLDER,
    ),
    margin = dict(
        t = 60,
        l = 40,
        b = 40,
        r = 40,
        pad = 0,
    ),
    hovermode = 'x',
    barmode = "group",
    # Color theme
    plot_bgcolor = _PLACEHOLDER,
    paper_bgcolor = _PLACEHOLDER,
    # Gaps
    bargap = 0.3,
    bargroupgap = 0.0,
    boxgap = 0.3,
    boxgroupgap = 0.0,
    # Legend
    showlegend = False,
    legend = dict(
        bgcolor = _PLACEHOLDER,
        x = 0.01,
        y = 0.99,
        xanchor = 'left',
        yanchor = 'top',
        tracegroupgap = 10,
        #font = dict(
        #    size = 10,
        #    color = _OPTIONAL,
        #),
    ),
)


SKELETON = {'base_colors': BASE_COLORS, 'base_traces': BASE_TRACES,
            'base_additions': BASE_ADDITIONS, 'base_layout': BASE_LAYOUT}
