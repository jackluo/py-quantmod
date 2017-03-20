
test1 = dict(
    a = 1,
    b = 2,
    c = dict(
        la = 1,
        si = 2,
    ),)

test2 = dict(
    a = dict(
        gagaga = 10,
        gaga = 9,
        basd = dict(
            aass = 10001,
        ),
    ),
    b = 4,)

test1.update(test2)
test1

def merge_dict(d1, d2):
    d = d2.copy()
    for k, v in list(d1.items()):
        if k not in d:
            d[k] = v
        else:
            if isinstance(v, dict):
                d[k] = merge_dict(d1[k], d[k])
    return d

merge_dict(test1, test2)

z = {**test1, **test2}
z

data[0]['line'].update(color=normalize(up_color))

class CufflinksError(Exception):
		pass


    if not isinstance(traces, list):
        traces = [traces]




def get_layout(base_traces, layout=None, **kwargs):
    """Generate a Plotly layout

    Parameters
    ----------
            theme : string
                Quantmod theme
            layout : dict or graph_objs.Layout
                Plotly layout dict or graph_objs.Layout figure

    """
    for key in kwargs.keys():
        if key not in _LAYOUT_KWARGS:
            raise Exception("Invalid keyword '{0}'.".format(key))

    if not theme:
        theme = auth.get_config_file()['theme']

    if layout:
        if not isinstance(layout, dict):
            try:
                layout = dict(layout.items())  # Coerce to regular dict
            except:
                raise Exception("Invalid layout '{0}'.".format(layout))




















'xlabel', 'ylabel', 'xitle', 'ytitle',
                          'xTitle', 'yTitle', 'xrange', 'yrange',
                          'log', 'xlog', 'ylog', 'logx', 'logy'}


xaxis_title : string
    BLABLA
yaxis_title : string
    BLABLA
xaxis_range : list
    BLABLA
yaxis_range : list
    BLABLA
xaxis_log : bool
    BLABLA
yaxis_log : bool
    BLABLA


            # Rename

            # Figsize argument is below
            if 'xlabel' in kwargs:
                xaxis_title = kwargs['xlabel']  # Matplotlib
            if 'xtitle' in kwargs:
                xaxis_title = kwargs['xtitle']  # Cufflinks
            if 'xTitle' in kwargs:
                xaxis_title = kwargs['xTitle']  # Cufflinks

            if 'xrange' in kwargs:
                xaxis_range = kwargs['xrange']
            if 'yrange' in kwargs:
                yaxis_range = kwargs['yrange']

            if 'log' in kwargs:
                yaxis_log = kwargs['log']

            if 'xlog' in kwargs:
                xaxis_log = kwargs['xlog']
            if 'logx' in kwargs:
                xaxis_log = kwargs['logx']

            if 'ylog' in kwargs:
                xaxis_log = kwargs['ylog']
            if 'logy' in kwargs:
                xaxis_log = kwargs['logy']



    if xaxis_title:
        if not isinstance(xaxis_title, six.string_types):
            raise Exception("Invalid xaxis_title '{0}'.".format(xaxis_title))

    if yaxis_title:
        if not isinstance(yaxis_title, six.string_types):
            raise Exception("Invalid yaxis_title '{0}'.".format(yaxis_title))

    # Test below items if list, else raise exception
    if xaxis_range:
        if not isinstance(xaxis_range, list):
            raise Exception("Invalid xaxis_range '{0}'.".format(xaxis_range))

    if yaxis_range:
        if not isinstance(yaxis_range, list):
            raise Exception("Invalid yaxis_range '{0}'.".format(yaxis_range))

    # Test below items if bool, else raise exception
    if xaxis_log:
        if not isinstance(xaxis_log, bool):
            raise Exception("Invalid xaxis_log '{0}'.".format(xaxis_log))

    if yaxis_log:
        if not isinstance(yaxis_log, bool):
            raise Exception("Invalid yaxis_log '{0}'.".format(yaxis_log))
