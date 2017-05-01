"""Core Quantmod functions

Contains some wrappers over 'chart.py' for those used to R's Quantmod style,
along with other tools for financial data acquisition.

"""
from __future__ import absolute_import

import six
import datetime as dt
import pandas_datareader.data as web

from .chart import Chart


def get_symbol(ticker, src='yahoo', start='01/01/2010',
               end=dt.datetime.today(), to_frame=False):
    """Get symbols

    Currently just a wrapper over pandas_datareader.data.DataReader.

    Parameters
    ----------
    ticker : string or list
        Stock ticker or list of stock tickers to fetch from.
    src : string, default 'yahoo'
        String specifying the data source to fetch data from.
    start : string or datetime
        Left boundary for date range, specified either as string or as a
        datetime object. Defaults to 1/1/2010.
    end : string or datetime
        Right boundary for date range, specified either as string or as a
        datetime object. Defaults to datetime.today().
    to_frame : bool, default False
        If True, returns obtained symbols as a DataFrame instead of a
        Quantmod Chart.

    Examples
    --------
    # Get Apple stock
    df = get_symbols('AAPL')

    # Get Apple stock from Google and return DataFrame
    df = get_symbols('AAPL', 'google', to_frame=True)

    # Get the VIX from Fred
    df = get_symbols('VIX', 'fred')

    Returns
    -------
    symbol : DataFrame

    """
    # Type checks for mandatorily used arguments
    if isinstance(ticker, six.string_types):
        pass
    elif isinstance(ticker, list):
        pass
    else:
        raise TypeError("Invalid ticker '{0}'. "
                        "It should be string or dict.".format(ticker))

    if isinstance(src, six.string_types):
        pass
    elif isinstance(src, dict):
        pass
    else:
        raise TypeError("Invalid src '{0}'. "
                        "It should be string or dict.".format(src))

    if isinstance(start, six.string_types):
        pass
    elif isinstance(start, dt.datetime) or isinstance(start, dt.date):
        pass
    else:
        raise TypeError("Invalid start '{0}'. "
                        "It should be string or datetime.".format(start))

    if isinstance(end, six.string_types):
        pass
    elif isinstance(end, dt.datetime) or isinstance(end, dt.date):
        pass
    else:
        raise TypeError("Invalid end '{0}'. "
                        "It should be string or datetime.".format(end))

    if not isinstance(to_frame, bool):
        raise TypeError("Invalid to_frame '{0}'. "
                        "It should be bool.".format(to_frame))

    symbols = web.DataReader(ticker, data_source=src, start=start, end=end)

    if not to_frame:
        symbols = Chart(symbols, ticker=ticker, src=src, start=start, end=end)

    return symbols


def chart_series(chart, iplot=False, **kwargs):
    """Wrapper over Chart.plot() and Chart.iplot().

    Parameters
    ----------
        chart : Quantmod Chart
            Quantmod Chart to plot with.
        iplot : bool, default False
            If True, plots chart for interactive display
            inside Jupyter notebooks instead of opening a browser HTML.

    """
    if not isinstance(chart, Chart):
        raise TypeError("Invalid chart '{0}'. "
                        "It should be Chart.".format(chart))

    if not isinstance(iplot, bool):
        raise TypeError("Invalid to_frame '{0}'. "
                        "It should be bool.".format(iplot))

    if iplot:
        Chart.iplot(**kwargs)
    else:
        Chart.plot(**kwargs)
