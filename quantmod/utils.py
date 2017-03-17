"""Low-level functions not meant for user access.

Used to maintain consistency for certain Python tasks.

"""
import collections


def strip_figure(figure):
    """Strip a Plotly figure into multiple figures with a trace on each of them.

    Parameters
    ----------
    figure : dict or Figure()
        Plotly figure

    """
    figures = []
    for trace in figure['data']:
        figures.append(dict(data=[trace], layout=figure['layout']))
    return figures


def get_base_layout(figures):
    """Generate a layout with the union of all properties of multiple figures' layouts.

    Parameters
    ----------
    figures : list(dict or Figure())
        List of Plotly figures

    """
    layout = {}
    for figure in figures:
        for key, value in list(figure['layout'].items()):
            layout[key] = value
    return layout


def update(dict1, dict2):
    """Recursivel update dict-like objects and returns it.

    Parameters
    ----------
            dict1 : dict
                    Dictionary that contains the values to update.
            dict2 : dict
                    Dictionary to be updated.

    """
    for key, value in dict2.items():
        if isinstance(value, collections.Mapping):
            temp = update(dict1.get(key, {}), value)
            dict1[key] = temp
        elif isinstance(dict1, collections.Mapping):
            dict1[key] = dict2[key]
        else:
            dict1 = {key: dict2[key]}

    return dict1


def deep_update(dict1, dict2):
    """Update the values (deep form) of a given dictionary and returns it.

    Parameters
    ----------
            dict1 : dict
                    Dictionary that contains the values to update.
            dict2 : dict
                    Dictionary to be updated.

    """
    for key, value in dict2.items():
        if isinstance(value, dict):
            if key in dict1:
                deep_update(dict1[key], value)
            else:
                dict1[key] = value
        else:
            dict1[key] = value

    return dict1
