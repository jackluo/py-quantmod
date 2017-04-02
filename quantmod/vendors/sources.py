"""Quandmod sources module

Sources are dicts that map OHLC column names to specific data vendors, e.g.
Bloomberg or Yahoo.

"""
# flake8: noqa

# Yahoo
YAHOO = dict(
    index = 'Date',
    op = 'Open',
    hi = 'High',
    lo = 'Low',
    cl = 'Close',
    aop = None,
    ahi = None,
    alo = None,
    acl = 'Adj Close',
    vo = 'Volume',
    di = None,
)

# Google
GOOGLE = dict(
    index = 'Date',
    op = 'Open',
    hi = 'High',
    lo = 'Low',
    cl = 'Close',
    aop = None,
    ahi = None,
    alo = None,
    acl = None,
    vo = 'Volume',
    di = None,
)

SOURCES = {'yahoo': YAHOO, 'google': GOOGLE}
