from .skeleton import base_template
from .skeleton import base_layout
from .colorscales import *


def get_light_theme():

    template = base_template

    template['candlestick']['increasing']['line']['color'] = '#00CC00'
    template['candlestick']['decreasing']['line']['color'] = '#FF7700'
    template['line']['marker']['color'] = 'blue'
    template['line']['line']['color'] = 'turquoise'
    template['bar']['marker']['color'] = 'red'

    template['xaxis']['rangeslider']['bordercolor'] = '#CCCCCC'
    template['xaxis']['rangeslider']['bgcolor'] = '#CCCCCC'

    template['xaxis']['rangeselector']['bordercolor'] = '#C9C9C9'
    template['xaxis']['rangeselector']['bgcolor'] = '#C9C9C9'
    template['xaxis']['rangeselector']['activecolor'] = '#888888'

    template['yaxis']['side'] = 'left'

    layout = base_layout

    layout['font']['family'] = 'droid mono'
    layout['font']['size'] = '12'
    layout['font']['color'] = '#000000'

    layout['plot_bgcolor'] = '#FFFFFF'
    layout['paper_bgcolor'] = '#F0F0F0'

    return template, layout
