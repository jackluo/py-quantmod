# Light Quantmod theme
LIGHT_QM = dict(

    colors = dict(
        increasing = '#00CC00',
        decreasing = '#FF7700',
        background = 'rgba(0,0,0,0.05)',
        primary = '#0D47EF',
        secondary = '#E13B30',
        tertiary = '#87F35C',
    ),

    traces = dict(
        line_thin = dict(width = 1,),
        line_thick = dict(width = 4,),
        line_dashed = dict(dash = 4,),
        line_dashed_thin = dict(dash = 4, width = 1,),
        line_dashed_thick = dict(dash = 4, width = 4,),
        area_dashed = dict(dash = 4),
    ),

    additions = dict(
        xaxis = dict(
            rangeslider = dict(
                bordercolor = '#CCCCCC',
                bgcolor = '#CCCCCC',
                thickness = 0.1,
            ),
            rangeselector = dict(
                bordercolor = '#C9C9C9',
                bgcolor = '#C9C9C9',
                activecolor = '#888888',
            ),
        ),
        yaxis = dict(side = 'left',),
    ),

    layout = dict(
        font = dict(
            family = 'droid sans mono',
            size = 12,
            color = '#000000',
        ),
        plot_bgcolor = '#FFFFFF',
        paper_bgcolor = '#F3F3F3',
    ),

)


# Dark Quantmod theme
DARK_QM = dict(

    colors = dict(
        increasing = '#00CC00',
        decreasing = '#FF7700',
        background = '#F3F3F3',
        primary = '#0D47EF',
        secondary = '#E13B30',
        tertiary = '#87F35C',
    ),

    traces = dict(
        line_thin = dict(width = 1,),
        line_thick = dict(width = 4,),
        line_dashed = dict(dash = 4,),
        line_dashed_thin = dict(dash = 4, width = 1,),
        line_dashed_thick = dict(dash = 4, width = 4,),
        area_dashed = dict(dash = 4),
    ),

    additions = dict(
        yaxis = dict(side = 'left',),
        rangeslider = dict(
            bordercolor = '#CCCCCC',
            bgcolor = '#CCCCCC',
            thickness = 0.1,
        ),
        rangeselector = dict(
            bordercolor = '#C9C9C9',
            bgcolor = '#C9C9C9',
            activecolor = '#888888',
        ),
    ),

    layout = dict(
        font = dict(
            family = 'droid sans mono',
            size = 12,
            color = '#000000',
        ),
        plot_bgcolor = '#FFFFFF',
        paper_bgcolor = '#F3F3F3',
    ),

)


THEMES = {'light': LIGHT_QM, 'dark': DARK_QM, 'light-qm': LIGHT_QM, 'dark-qm': DARK_QM}
