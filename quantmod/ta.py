"""Wrappers around Ta-Lib technical indicators

Python native indicators in 'tanolib.py' file.

"""
import talib


# Overlap studies
def add_SMA(self, timeperiod=30):
    """Simple moving average."""
    name = 'SMA({})'.format(str(timeperiod))
    self.pri[name] = dict(type='line', color='secondary')
    self.ind[name] = talib.SMA(self.df[self.cl].values, timeperiod)


def add_EMA(self, timeperiod=30):
    """Exponential moving average."""
    name = 'EMA({})'.format(str(timeperiod))
    self.pri[name] = dict(type='line', color='secondary')
    self.ind[name] = talib.EMA(self.df[self.cl].values, timeperiod)


def add_WMA(self, timeperiod=30):
    """Weighted moving average."""
    name = 'WMA({})'.format(str(timeperiod))
    self.pri[name] = dict(type='line', color='secondary')
    self.ind[name] = talib.WMA(self.df[self.cl].values, timeperiod)


def add_DEMA(self, timeperiod=30):
    """Double exponential moving average."""
    name = 'DEMA({})'.format(str(timeperiod))
    self.pri[name] = dict(type='line', color='secondary')
    self.ind[name] = talib.DEMA(self.df[self.cl].values, timeperiod)


def add_TEMA(self, timeperiod=30):
    """Triple moving exponential average."""
    name = 'TEMA({})'.format(str(timeperiod))
    self.pri[name] = dict(type='line', color='secondary')
    self.ind[name] = talib.TEMA(self.df[self.cl].values, timeperiod)


def add_KAMA(self, timeperiod=30):
    """Kaufmann adaptive moving average."""
    name = 'KAMA({})'.format(str(timeperiod))
    self.pri[name] = dict(type='line', color='secondary')
    self.ind[name] = talib.KAMA(self.df[self.cl].values, timeperiod)


def add_TRIMA(self, timeperiod=30):
    """Triangular moving average."""
    name = 'TRIMA({})'.format(str(timeperiod))
    self.pri[name] = dict(type='line', color='secondary')
    self.ind[name] = talib.TRIMA(self.df[self.cl].values, timeperiod)


def add_MA(self, timeperiod=30, matype=0):
    """Moving average (customizable)."""
    name = 'MA({})'.format(str(timeperiod))
    self.pri[name] = dict(type='line', color='secondary')
    self.ind[name] = talib.MA(self.df[self.cl].values, timeperiod, matype)


def add_BBANDS(self, timeperiod=5, nbdevup=2, nbdevdn=2, matype=0):
    """Bollinger bands."""
    name = 'BB({},{},{})'.format(str(timeperiod), str(nbdevup), str(nbdevdn))
    ubb = 'U' + name
    bb = name
    lbb = 'L' + name
    self.pri[ubb] = dict(type='line_dashed_thin', color='tertiary')
    self.pri[bb] = dict(type='area_dashed_thin', color='grey', fillcolor='fill')  # noqa: E501
    self.pri[lbb] = dict(type='area_dashed_thin', color='tertiary', fillcolor='fill')  # noqa: E501
    self.ind[ubb], self.ind[bb], self.ind[lbb] = talib.BBANDS(self.df[self.cl].values, timeperiod, nbdevup, nbdevdn, matype)  # noqa: E501


def add_MAMA(self):
    pass


def add_MAVP(self, periods, inperiod=2, maxperiod=30, matype=0):
    pass


def add_RSI(self, timeperiod=14):
    name = 'RSI({})'.format(str(timeperiod))
    self.sec[name] = dict(type='line', color='secondary')
    self.ind[name] = talib.RSI(self.df[self.cl].values, timeperiod)
