_PLACEHOLDER = False


# TRACE PRIMITIVES
BASE_TRACES = dict(

    candlestick = dict(

        type = 'candlestick',
        hoverinfo = "x+y+text+name",

        # INCREASING
        increasing = dict(
            line = dict(
                width = 2,
                color = _PLACEHOLDER,
            ),
        ),

        # DECREASING
        decreasing = dict(
            line = dict(
                width = 2,
                color = _PLACEHOLDER,
            ),
        ),

    ),

    line = dict(

        type = 'scatter',
        hoverinfo = "x+y+text+name",
        mode = "lines",
        #fill = 'tonexty',
        opacity = 0.6,

        # MARKER
        marker = dict(
            size = 6,
            opacity = 0.8,
            symbol = "square",
            color = _PLACEHOLDER,
        ),

        # LINE
        line = dict(
            width = 2,
            color = _PLACEHOLDER,
            #dash = 4,
            #shape = "spline",
            #smoothing = "2",
        ),

        # AREA
        fillcolor = _PLACEHOLDER,

    ),

    bar = dict(

        type = 'bar',
        hoverinfo = "x+y+text+name",
        mode = "markers",

        # MARKER
        marker = dict(
            size = 5,
            opacity = 0.8,
            symbol = "square",
            color = _PLACEHOLDER,
        ),

    ),

)


# LAYOUT MODIFIERS
BASE_ADDITIONS = dict(

    xaxis = dict(

        # RANGE
        #nticks = , #OR
        #tick0 = , #AND
        #dtick = ,

        # RANGE SLIDER AND SELECTOR
        rangeslider = dict(
            visible = False,
            bordercolor = _PLACEHOLDER,
            bgcolor = _PLACEHOLDER,
            thickness = 0.1,
        ),

        rangeselector = dict(
            visible = True,
            bordercolor = _PLACEHOLDER,
            bgcolor = _PLACEHOLDER,
            activecolor = _PLACEHOLDER,
        ),

        # TICKS
        #tickfont = dict(size = 10),
        #showticklabels = False,

        # OTHER
        side = "bottom",
        #showline = False,
        #showgrid = False,
        #zeroline = False,
        #titlefont = dict(size = 10),

    ),

    yaxis = dict(

        # RANGE
        #rangemode = "tozero",
        #range = ,
        #nticks = , #OR
        #tick0 = , #AND
        #dtick = ,

        # TICKS
        #tickfont = dict(size = 10),
        #showticklabels = False,

        # OTHER
        type = "linear",
        domain = [0.0, 1],
        side = "right",
        #showline = False,
        #showgrid = False,
        #zeroline = False,
        #titlefont = dict(size = 10),

    ),

    buttons = [
        dict(count = 1, step = "day", stepmode = "backward", label = "1D"),
        dict(count = 5, step = "day", stepmode = "backward", label = "5D"),
        dict(count = 1, step = "month", stepmode = "backward", label = "1M"),
        dict(count = 3, step = "month", stepmode = "backward", label = "3M"),
        dict(count = 6, step = "month", stepmode = "backward", label = "6M"),
        dict(count = 1, step = "year", stepmode = "backward", label = "1Y"),
        dict(count = 2, step = "year", stepmode = "backward", label = "2Y"),
        dict(count = 5, step = "year", stepmode = "backward", label = "5Y"),
        dict(count = 1, step = "all", stepmode = "backward", label = "MAX"),
        dict(count = 1, step = "year", stepmode = "todate", label = "YTD"),
    ],

)


# LAYOUT PRIMITIVES
BASE_LAYOUT = dict(

    title = "",

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
    #hovermode = False,

    # COLOR THEME
    plot_bgcolor = _PLACEHOLDER,
    paper_bgcolor = _PLACEHOLDER,

    # LEGEND
    showlegend = False,
    legend = dict(
        x = 1.02,
        y = 1,
        tracegroupgap = 10,
        #font = dict(
        #    size = 10,
        #    color = _OPTIONAL,
        #),
    ),

)


SKELETON = {'base_traces': BASE_TRACES, 'base_additions': BASE_ADDITIONS, 'base_layout': BASE_LAYOUT}
