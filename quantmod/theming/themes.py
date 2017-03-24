"""Quandmod themes module

Create your own modules by copying one of the themes and editing it after.
Make sure that colors, traces, additions and layout are all under one main dict,
and add that dict to '_VALID_THEMES' at the bottom of the file.

For readability, files under theming do not follow PEP8 guideline of
no space between assignment of named arguments.

"""
from __future__ import absolute_import

from .palettes import LIGHT_PALETTE, DARK_PALETTE


# Light Quantmod theme
LIGHT_QM = dict(

    colors = dict(
        increasing = '#00CC00',
        decreasing = '#FF7700',
        border = LIGHT_PALETTE['grey25'],
        primary = '#0D47EF',
        secondary = '#E13B30',
        tertiary = '#87F35C',
        grey = LIGHT_PALETTE['grey25'],
        grey_light = LIGHT_PALETTE['grey15'],
        grey_strong = LIGHT_PALETTE['grey40'],
        fill = LIGHT_PALETTE['grey05'],
        fill_light = LIGHT_PALETTE['grey02'],
        fill_strong = LIGHT_PALETTE['grey10'],
    ),

    traces = dict(
        line_thin = dict(width = 1,),
        line_thick = dict(width = 4,),
        line_dashed = dict(dash = 5,),
        line_dashed_thin = dict(dash = 5, width = 1,),
        line_dashed_thick = dict(dash = 5, width = 4,),
        area_dashed = dict(dash = 5,),
        area_dashed_thin = dict(dash = 5, width = 1,),
        area_dashed_thick = dict(dash = 5, width = 4,),
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
        legend = dict(
            bgcolor = LIGHT_PALETTE['transparent'],
        ),
    ),

)


THEMES = {'light': LIGHT_QM} #, 'dark': DARK_QM, 'light-qm': LIGHT_QM, 'dark-qm': DARK_QM}
