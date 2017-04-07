"""Low-level functions not meant for user access

Functions used to maintain consistency for certain Python tasks,
e.g. type checking of function arguments. Users should not expect any function
inside this module to keep a consistent API, as they are only used internally.

"""
from __future__ import absolute_import

import collections
import json
import os


def update(dict1, dict2):
    """Recursivel update dict-like objects and returns it.

    Need return to work properly even though dict1 is updated inplace.

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

    Need return to work properly even though dict1 is updated inplace.

    Parameters
    ----------
        dict1 : dict
            Dictionary that contains the values to update.
        dict2 : dict
            Dictionary to be updated.

    """
    for key, value in dict2.items():
        if isinstance(value, collections.Mapping):
            if key in dict1:
                deep_update(dict1[key], value)
            else:
                dict1[key] = value
        else:
            dict1[key] = value

    return dict1


def type_check(arg, arg_types, arg_name):
    """Check if argument is of one or multiple allowed types.

    Pass if argument is within an allowed type, and raise exception
    if argument is not within these types, thus allowing for
    strong typing of Python arguments.

    Parameters
    ----------
        arg : [any type]
            Argument that can be of any type.
        arg_types : list or [any type]
            Type or list of allowed argument types.
        arg_name : string
            Name of argument to be printed in exception.

    Example
    -------
        layout = dict(title='Test', showlegend=False)
        typecheck(layout, dict, 'layout') # pass

    """
    if not isinstance(arg_types, list):
        arg_types = [arg_types]

        if any(isinstance(arg, arg_type) for arg_type in arg_types):
            pass
        else:
            raise Exception("Invalid {0} '{1}'.".format(arg_name, arg))


def kwargs_check(kwargs, validator):
    """Check kwargs for validity

    Parameters
    ----------
        kwargs : dict
            Keyword arguments to check for validity.
        validator : iterable
            Iterable of valid arguments to check from.

    """
    for key in kwargs:
        if key not in validator:
            raise Exception("Invalid keyword '{0}'.".format(key))


def parse(kwargs, dict):
    """Parse kwargs into input dict.

    Parameters
    ----------
        kwargs : dict
            Keyword arguments to update dict with
        dict : dict
            Dict to update with keyword arguments

    """
    for key in kwargs:
        dict[key] = kwargs[key]


def kwargs_from_keyword(keyword, from_kwargs, to_kwargs=None, inplace=False):
    """Look for keys of the format keyword_value.

    Return a dictionary with {keyword: value} format.

    Parameters
    ----------
        keyword : string
            Keyword to look for in the orginal dictionary.
        from_kwargs : dict
            Original dictionary.
        to_kwargs : dict
            Dictionary where the items will be appended.
        inplace : bool
            If True then the key, value pairs from the original
            dictionary are modified.

    """
    if not inplace:
        if to_kwargs is None:
            to_kwargs = {}

    keys = set(from_kwargs.keys())

    for key in keys:
        if '{0}_'.format(keyword) in key:
            updated_key = key.replace('{0}_'.format(keyword), '')
            if inplace:
                from_kwargs[updated_key] = from_kwargs[key]
                del from_kwargs[key]
            else:
                to_kwargs[updated_key] = from_kwargs[key]

    if not inplace:
        return to_kwargs


def load_json_dict(filename, *args):
    """Check if file exists. Return {} if something fails.

    Parameters
    ----------
        filename : string
            Filename of file to check.

    """
    data = {}
    if os.path.exists(filename):
        with open(filename, "r") as f:
            try:
                data = json.load(f)
                if not isinstance(data, dict):
                    data = {}
            except:
                pass
        if args:
            return {key: data[key] for key in args if key in data}
    return data


def save_json_dict(filename, json_dict):
    """Will error if filename is not appropriate, but it's checked elsewhere.

    Parameters
    ----------
        filename : string
            Filename of json_dict to save.
        json_dict : dict
            Dict that will be saved as json.

    """
    if isinstance(json_dict, dict):
        with open(filename, 'w') as f:
            f.write(json.dumps(json_dict, indent=4))
    else:
        raise TypeError("Couldn't save because 'json_dict' "
                        "was not a dictionary.")
