from copy import deepcopy

from .template import base_traces
from .template import base_additions
from .template import base_layout


def get_light_theme():

    colors = dict(
        increasing = '#00CC00',
        decreasing = '#FF7700',
        background = '#F3F3F3',
        blue = '#0D47EF',
        red = '#E13B30', # Should ideally contrast with trace1
        green = '#87F35C', # Should ideally contrast with trace1 and trace2
    )


    # FULL TRACES
    traces = base_traces

    traces['candlestick']

    traces['line']

    traces['scatter'] = deepcopy(traces['line'])
    traces['scatter']['mode'] = 'markers'

    traces['line-thick'] = deepcopy(traces['line'])
    traces['line-thick']['line']['width'] = 4

    traces['line-thin'] = deepcopy(traces['line'])
    traces['line-thin']['line']['width'] = 1

    traces['line-dashed'] = deepcopy(traces['line'])
    traces['line-dashed']['line']['dash'] = 4

    traces['line-dashed-thick'] = deepcopy(traces['line-dashed'])
    traces['line-dashed-thick']['line']['dash'] = 4
    traces['line-dashed-thick']['line']['width'] = 4

    traces['line-dashed-thin'] = deepcopy(traces['line-dashed'])
    traces['line-dashed-thin']['line']['dash'] = 4
    traces['line-dashed-thin']['line']['width'] = 1

    traces['area'] = deepcopy(traces['line'])
    traces['area']['fill'] = 'tonexty'

    traces['area-dashed'] = deepcopy(traces['area'])
    traces['area-dashed']['line']['dash'] = 4

    traces['area-threshold'] = deepcopy(traces['area'])

    traces['bar']

    traces['histogram'] = deepcopy(traces['bar'])


    # LAYOUT ADDITIONS
    additions = base_additions
    additions['xaxis']['rangeslider']['bordercolor'] = '#CCCCCC'
    additions['xaxis']['rangeslider']['bgcolor'] = '#CCCCCC'

    additions['xaxis']['rangeselector']['bordercolor'] = '#C9C9C9'
    additions['xaxis']['rangeselector']['bgcolor'] = '#C9C9C9'
    additions['xaxis']['rangeselector']['activecolor'] = '#888888'

    additions['yaxis']['side'] = 'left'


    # LAYOUT
    layout = base_layout

    layout['font']['family'] = 'droid sans mono'
    layout['font']['size'] = '12'
    layout['font']['color'] = '#000000'

    layout['plot_bgcolor'] = '#FFFFFF'
    layout['paper_bgcolor'] = '#F3F3F3'


    return colors, traces, additions, layout
