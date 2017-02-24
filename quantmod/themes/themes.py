from .skeleton import base_template
from .skeleton import base_layout
from .colorscales import *


def get_light_theme():

    tracecolors = dict(

        increasing = '#00CC00',
        decreasing = '#FF7700',
        background = '#F3F3F3',
        trace1 = '#3262A6',
        trace2 = '#FC0D1B',
        trace3 = '#09630C',

    )

    template = base_template

    # TRACE PRIMITIVES
    template['candlestick']['increasing']['line']['color'] = tracecolors['increasing']
    template['candlestick']['decreasing']['line']['color'] = tracecolors['decreasing']

    template['line1']['marker']['color'] = '#3262A6'
    template['line1']['line']['color'] = '#3262A6'

    template['line2'] = template['line']
    template['line2']['']

    #L2 (dashed line)

    #

    template['bar']['marker']['color'] = 'red'

    # LAYOUT MODIFIERS
    template['xaxis']['rangeslider']['bordercolor'] = '#CCCCCC'
    template['xaxis']['rangeslider']['bgcolor'] = '#CCCCCC'

    template['xaxis']['rangeselector']['bordercolor'] = '#C9C9C9'
    template['xaxis']['rangeselector']['bgcolor'] = '#C9C9C9'
    template['xaxis']['rangeselector']['activecolor'] = '#888888'

    template['yaxis']['side'] = 'left'

    layout = base_layout

    layout['font']['family'] = 'droid sans mono'
    layout['font']['size'] = '12'
    layout['font']['color'] = '#000000'

    layout['plot_bgcolor'] = '#FFFFFF'
    layout['paper_bgcolor'] = '#F0F0F0'

    return template, layout


def generate_template(colors):

    # COLORS
    colors = dict(

        increasing = _PLACEHOLDER,
        decreasing = _PLACEHOLDER,
        line = _PLACEHOLDER,
        line2 = _PLACEHOLDER,
        line3 = _PLACEHOLDER,
        area = _PLACEHOLDER,
        fontcolor = '#000000',
        p


    )
