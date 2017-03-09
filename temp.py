
def make_full_layout():

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


    # ADDITIONS
    additions['yaxis']['side'] = 'left'


    # LAYOUT
    layout = base_layout

    layout['font']['family'] = 'droid sans mono'
    layout['font']['size'] = '12'
    layout['font']['color'] = '#000000'

    layout['plot_bgcolor'] = '#FFFFFF'
    layout['paper_bgcolor'] = '#F3F3F3'
