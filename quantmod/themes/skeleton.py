_PLACEHOLDER = False
_OPTIONAL = False

theme = dict(

    trace = dict(

        hoverinfo = "x+y+text+name",
        mode = "lines",
        marker = dict(
            size = 5,
            opacity = 0.8,
            symbol = "square",
            color = _PLACEHOLDER,
        )
        line = dict(
            width = 2,
            color = _PLACEHOLDER,
            #shape =  "spline",
            #smoothing = "2",
            #dash = 4,
        )
        fill =
        fillcolor =

    ),

    layout = dict(

        title = "",

        # GENERAL LAYOUT
        width = 1080,
        height = 720,
        autosize = True,
        font = dict(
            family = "Overpass",
            size = 12,
            color = _PLACEHOLDER,
        ),
        margin = dict(
            t = 40,
            l = 40,
            b = 40,
            r = 40,
            pad = 0,
        ),
        showlegend = False,
        hovermode = False,

        # OPTIONAL
        annotations = _OPTIONAL, # list()
        shapes = _OPTIONAL, # list()
        images = _OPTIONAL, # list()

        # COLOR THEME
        plot_bgcolor = _PLACEHOLDER,
        paper_bgcolor = _PLACEHOLDER,

        # LEGEND
        legend = dict(
            x = 1.02,
            y = 1,
            tracegroupgap = 10,
            #font = dict(
            #    size = 10
            #    color = _OPTIONAL,
            #),
        ),

        # LINEAR PLOTS
        xaxis = dict(

            # RANGE
            #nticks = , #OR
            #tick0 = , #AND
            #dtick = ,

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
        yaxis2 = dict(

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
            domain = [0.0, 0.0],
            side = "right",
            #showline = False,
            #showgrid = False,
            #zeroline = False,
            #titlefont = dict(size = 10),

        ),
        # BAR PLOTS
        barmode = "group",

        ),
        yaxis3 = dict(

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
            domain = [0.0, 0.0],
            side = "right",
            #showline = False,
            #showgrid = False,
            #zeroline = False,
            #titlefont = dict(size = 10),

        ),
        # BAR PLOTS
        barmode = "group",

        ),

    ),

)
