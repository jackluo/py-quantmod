"""Based on Plotly's tools module"""
import os
import json
import warnings
from offline import go_offline


package = 'quantmod'


dropbox_path = 'Programs/Data'
if dropbox_path:
    AUTH_DIR = os.path.join(os.path.join(os.path.expanduser('~'),
                                         os.path.join('Dropbox', dropbox_path)), package)
else:
    AUTH_DIR = os.path.join(os.path.expanduser('~'), '.' + package)

TEST_DIR = os.path.join(AUTH_DIR, 'test')
TEST_FILE = os.path.join(AUTH_DIR, 'permission_test')
# PICKLE_FILE = os.path.join(AUTH_DIR, 'pickle') # Unused
# CREDENTIALS_FILE = os.path.join(AUTH_DIR, 'credentials.json') # Unused
CONFIG_FILE = os.path.join(AUTH_DIR, 'config.json')

_FILE_CONTENT = {
    CONFIG_FILE: {
        'sharing': 'public',
        'theme': 'light-qm',
        'dimensions': None,
        'offline': False,
        'offline_url': '',
        'offline_show_link': True,
        'offline_link_text': "Export to plot.ly",
    }
}


try:
    """Permissions test."""
    if not os.path.exists(AUTH_DIR):
        os.mkdir(AUTH_DIR) # Auth dir

    os.mkdir(TEST_DIR) # Test directory
    os.rmdir(TEST_DIR)

    f = open(TEST_FILE, 'w') # Test file
    f.write("Testing write permissions.\n")
    f.close()
    os.remove(TEST_FILE)

    _file_permissions = True

except:
    _file_permissions = False


def get_path():
    """Get path of AUTH_DIR."""
    return AUTH_DIR


def get_pickle_path():
    """Get path of the pickle file."""
    return PICKLE_FILE


def check_file_permissions():
    """Returns True if write permissions, else returns False."""
    return _file_permissions


def ensure_local_files():
    """Ensure that filesystem is setup/filled out in a valid way."""
    if _file_permissions:
        if not os.path.isdir(AUTH_DIR):
            os.mkdir(AUTH_DIR)
        for fn in [CONFIG_FILE]:
            contents = load_json_dict(fn)
            for key, value in list(_FILE_CONTENT[fn].items()):
                if key not in contents:
                    contents[key] = value
            contents_keys = list(contents.keys())
            for key in contents_keys:
                if key not in _FILE_CONTENT[fn]:
                    del contents[key]
            save_json_dict(fn, contents)
    else:
        warnings.warn("Looks like you don't have 'read-write' permission to \
        your specified Dropbox folder or home ('~') directory")


def load_json_dict(filename, *args):
    """Checks if file exists. Returns {} if something fails."""

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
    """Will error if filename is not appropriate, but it's checked elsewhere."""

    if isinstance(json_dict, dict):
        with open(filename, 'w') as f:
            f.write(json.dumps(json_dict, indent=4))
    else:
        raise TypeError("Couldn't save because 'json_dict' was not a dictionary.")


def get_config_file(*args):
    """
    Return specified args from `~/config`. as dict.
    Returns all if no arguments are specified.

    Example
    -------
        get_config_file('sharing')

    """
    if _file_permissions:
        ensure_local_files()
        return load_json_dict(CONFIG_FILE, *args)
    else:
        return _FILE_CONTENT[CONFIG_FILE]


def set_config_file(sharing=None, theme=None, dimensions=None,
                    offline=None, offline_url=None,
                    offline_show_link=None, offline_link_text=None, **kwargs):
    """Set the keyword-value pairs in `~/config`.

    Parameters
    ----------
        sharing : string
                        Sets the sharing level permission
                                public - anyone can see this chart
                                private - only you can see this chart
                                secret - only people with the link can see the chart
        theme : string
                        Sets the default theme
                        See tools.get_themes() for available themes
        dimensions : tuple
                        Sets the default (width, height) of the chart
        offline : bool
                        If true then the charts are rendered
                        locally.
        offline_show_link : bool
                        If true then the chart will show a link to
                        plot.ly at the bottom right of the chart
        offline_link_text : string
                        Text to display as link at the bottom
                        right of the chart

    """
    if not _file_permissions:
        raise Exception("You don't have proper file permissions to run this function.")

    valid_kwargs = ['world_readable', 'dimensions']

    for key in list(kwargs.keys()):
        if key not in valid_kwargs:
            raise Exception('Invalid keyword "{0}"'.format(key))

    config = get_config_file()

    if isinstance(sharing, bool):
        if sharing:
            sharing = 'public'
        else:
            sharing = 'private'

    if sharing:
        config['sharing'] = sharing
    if theme:
        config['theme'] = theme
    if dimensions:
        config['dimensions'] = dimensions
    if offline:
        config['offline'] = offline
        if offline:
            go_offline()
    if offline_url:
        config['offline_url'] = offline_url
    if offline_show_link:
        config['offline_show_link'] = offline_show_link
    if offline_link_text:
        config['offline_link_text'] = offline_link_text

    save_json_dict(CONFIG_FILE, config)
    ensure_local_files()
