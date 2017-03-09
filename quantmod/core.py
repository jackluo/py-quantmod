import pandas_datareader.data as web


def get_symbol(ticker, src='yahoo', start=None, end=None):
    """Get symbols as a DataFrame.

    Currently just a wrapper over pandas_datareader.data.DataReader.

    Parameters
    ----------
    ticker : str or list of strs
        Stock ticker or list of stock tickers to fetch from.
    src : str, optional
        The data source to fetch data from.
    start : datetime, optional
        Left boundary for date range. Defaults to 1/1/2010.
    end : datetime, optional
        Right boundary for date range. Defaults to today.

    Examples
    --------

    # Get Apple stock
    df = get_symbols('AAPL')

    # Get Apple stock from Google
    df = get_symbols('AAPL', 'google')

    # Get the VIX from Fred
    df = get_symbols('VIX', 'fred')

    Returns
    -------
    symbol : DataFrame

    """

    symbols = web.DataReader(ticker, src, start, end)
    return symbols


def chart_series(Chart):
    Chart.plot()
