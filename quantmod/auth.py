"""Functions that manage configuration writing

Refactored from Plotly's 'auth.py'.

"""
from __future__ import absolute_import

import os


package = 'quantmod'

AUTH_DIR = os.path.join(os.path.expanduser('~'), '.' + package)
TEST_DIR = os.path.join(AUTH_DIR, 'test')
TEST_FILE = os.path.join(AUTH_DIR, 'permission_test')
CONFIG_FILE = os.path.join(AUTH_DIR, 'config.json')

FILE_CONTENT = {
    CONFIG_FILE: {
        'sharing': 'public',
        'dimensions': None,
        'theme': 'light',
        'source': 'yahoo',
        'offline': False,
        'offline_url': '',
        'offline_show_link': True,
        'offline_link_text': 'Edit Chart',
    }
}


def _permissions():
    """Check for write access."""
    try:
        os.mkdir(TEST_DIR)
        os.rmdir(TEST_DIR)
        if not os.path.exists(AUTH_DIR):
            os.mkdir(AUTH_DIR)
        with open(TEST_FILE, 'w') as f:
            f.write('Testing\n')
        os.remove(TEST_FILE)
        return True
    except:
        return False


_file_permissions = _permissions()


def check_file_permissions():
    """Return True if write permissions, else return False."""
    return _file_permissions


def get_path():
    """Get path of AUTH_DIR."""
    return AUTH_DIR
