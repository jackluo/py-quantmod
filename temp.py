
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
