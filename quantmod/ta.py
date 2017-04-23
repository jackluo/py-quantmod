"""Wrappers around Ta-Lib technical indicators

Python native indicators in 'tanolib.py' file.

"""
import numpy as np
import pandas as pd
import talib

from . import utils
from .valid import VALID_TA_KWARGS


# Overlap studies


def add_MA(self, timeperiod=20, matype=0,
           type='line', color='secondary', **kwargs):
    """Moving average (customizable)."""

    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'MA({})'.format(str(timeperiod))
    self.pri[name] = dict(type=type, color=color)
    self.ind[name] = talib.MA(self.df[self.cl].values, timeperiod, matype)


def add_SMA(self, timeperiod=20,
            type='line', color='secondary', **kwargs):
    """Simple moving average."""

    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'SMA({})'.format(str(timeperiod))
    self.pri[name] = dict(type=type, color=color)
    self.ind[name] = talib.SMA(self.df[self.cl].values, timeperiod)


def add_EMA(self, timeperiod=26,
            type='line', color='secondary', **kwargs):
    """Exponential moving average."""

    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'EMA({})'.format(str(timeperiod))
    self.pri[name] = dict(type=type, color=color)
    self.ind[name] = talib.EMA(self.df[self.cl].values, timeperiod)


def add_WMA(self, timeperiod=20,
            type='line', color='secondary', **kwargs):
    """Weighted moving average."""

    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'WMA({})'.format(str(timeperiod))
    self.pri[name] = dict(type=type, color=color)
    self.ind[name] = talib.WMA(self.df[self.cl].values, timeperiod)


def add_DEMA(self, timeperiod=26,
             type='line', color='secondary', **kwargs):
    """Double exponential moving average."""

    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'DEMA({})'.format(str(timeperiod))
    self.pri[name] = dict(type=type, color=color)
    self.ind[name] = talib.DEMA(self.df[self.cl].values, timeperiod)


def add_TEMA(self, timeperiod=26,
             type='line', color='secondary', **kwargs):
    """Triple moving exponential average."""

    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'TEMA({})'.format(str(timeperiod))
    self.pri[name] = dict(type=type, color=color)
    self.ind[name] = talib.TEMA(self.df[self.cl].values, timeperiod)


def add_T3(self, timeperiod=20, vfactor=0.7,
           type='line', color='secondary', **kwargs):
    """T3 Exponential Moving Average."""

    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'T3({}, {})'.format(str(timeperiod), str(vfactor))
    self.pri[name] = dict(type=type, color=color)
    self.ind[name] = talib.T3(self.df[self.cl].values, timeperiod, vfactor)


def add_KAMA(self, timeperiod=20,
             type='line', color='secondary', **kwargs):
    """Kaufmann adaptive moving average."""

    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'KAMA({})'.format(str(timeperiod))
    self.pri[name] = dict(type=type, color=color)
    self.ind[name] = talib.KAMA(self.df[self.cl].values, timeperiod)


def add_TRIMA(self, timeperiod=20,
              type='line', color='secondary', **kwargs):
    """Triangular moving average."""

    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'TRIMA({})'.format(str(timeperiod))
    self.pri[name] = dict(type=type, color=color)
    self.ind[name] = talib.TRIMA(self.df[self.cl].values, timeperiod)


def add_MAMA(self, fastlimit=0.5, slowlimit=0.05,
             types=['line', 'line'], colors=['secondary', 'tertiary'],
             **kwargs):
    """MESA Adaptive Moving Average.

    Note that the first argument of types and colors refers to MAMA while the
    second argument refers to FAMA.

    """
    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        kwargs['type'] = kwargs['kind']
    if 'kinds' in kwargs:
        types = kwargs['type']

    if 'color' in kwargs:
        colors = [kwargs['color'], kwargs['color']]
    if 'type' in kwargs:
        types = [kwargs['type'], kwargs['type']]

    mama = 'MAMA({}, {})'.format(str(fastlimit), str(slowlimit))
    fama = 'FAMA({}, {})'.format(str(fastlimit), str(slowlimit))
    self.pri[mama] = dict(type=types[0], color=colors[0])
    self.pri[fama] = dict(type=types[1], color=colors[1])
    self.ind[mama], self.ind[fama] = talib.MAMA(self.df[self.cl].values,
                                                fastlimit, slowlimit)


def add_MAVP(self, periods, minperiod=2, maxperiod=30, matype=0,
             type='line', color='secondary', **kwargs):
    """Moving average with variable period.

    Parameters
    ----------

        periods : Series or array
            Moving Average period over timeframe to analyze, as a 1-dimensional
            shape of same length as chart.

    """
    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    if isinstance(periods, pd.Series):
        periods = periods.values
    elif isinstance(periods, np.ndarray):
        pass
    else:
        raise TypeError("Invalid periods {0}. "
                        "It should be Series or array."
                        .format(periods))

    name = 'MAVP({}, {})'.format(str(minperiod), str(maxperiod))
    self.pri[name] = dict(type=type, color=color)
    self.ind[name] = talib.MAVP(self.df[self.cl].values,
                                periods, minperiod, maxperiod, matype)


def add_MIDPOINT(self, timeperiod=14,
                 type='line', color='secondary', **kwargs):
    """Midpoint price over period."""

    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'Midpoint({})'.format(str(timeperiod))
    self.pri[name] = dict(type=type, color=color)
    self.ind[name] = talib.MIDPOINT(self.df[self.cl].values)


def add_BBANDS(self, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0,
               types=['line_dashed_thin', 'line_dashed_thin'],
               colors=['tertiary', 'grey'], fillcolor='fill',
               **kwargs):
    """Bollinger bands.

    Note that the first argument of types and colors refers to upper and lower
    bands while second argument refers to middle band. (Upper and lower are
    symmetrical arguments, hence only 2 needed.)

    """
    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        kwargs['type'] = kwargs['kind']
    if 'kinds' in kwargs:
        types = kwargs['type']

    if 'color' in kwargs:
        colors = [kwargs['color'], kwargs['color']]
    if 'type' in kwargs:
        types = [kwargs['type'], kwargs['type']]

    name = 'BB({},{},{})'.format(str(timeperiod), str(nbdevup), str(nbdevdn))
    ubb = name + '[Upper]'
    bb = name
    lbb = name + '[Lower]'
    self.pri[ubb] = dict(type='line_' + types[0][5:],
                         color=colors[0])
    self.pri[bb] = dict(type='area_' + types[1][5:],
                        color=colors[1], fillcolor=fillcolor)
    self.pri[lbb] = dict(type='area_' + types[0][5:],
                         color=colors[0], fillcolor=fillcolor)
    (self.ind[ubb],
     self.ind[bb],
     self.ind[lbb]) = talib.BBANDS(self.df[self.cl].values,
                                   timeperiod, nbdevup, nbdevdn, matype)


def add_SAR(self, acceleration=0.02, maximum=0.20,
            type='scatter', color='tertiary', **kwargs):
    """Parabolic SAR."""

    if not (self.has_high and self.has_low):
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'SAR({}, {})'.format(str(acceleration), str(maximum))
    self.pri[name] = dict(type=type, color=color)
    self.ind[name] = talib.SAR(self.df[self.hi].values,
                               self.df[self.lo].values,
                               acceleration, maximum)


def add_SAREXT(self, startvalue=0, offsetonreverse=0,
               accelerationinitlong=0.02, accelerationlong=0.02,
               accelerationmaxlong=0.20, accelerationinitshort=0.02,
               accelerationshort=0.02, accelerationmaxshort=0.20,
               type='scatter', color='tertiary', **kwargs):
    """Parabolic SAR Extended."""

    if not (self.has_high and self.has_low):
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = ('SAREXT({}, {}, {}, {},'
            '{}, {}, {}, {})'.format(str(startvalue), str(offsetonreverse),
                                     str(accelerationinitlong),
                                     str(accelerationlong),
                                     str(accelerationmaxlong),
                                     str(accelerationinitshort),
                                     str(accelerationshort),
                                     str(accelerationmaxshort)))
    self.pri[name] = dict(type=type, color=color)
    self.ind[name] = talib.SAREXT(self.df[self.hi].values,
                                  self.df[self.lo].values,
                                  startvalue, offsetonreverse,
                                  accelerationinitlong,
                                  accelerationlong,
                                  accelerationmaxlong,
                                  accelerationinitshort,
                                  accelerationshort,
                                  accelerationmaxshort)
    self.ind[name] = self.ind[name].abs()  # Bug right now with negative value


def add_HT_TRENDLINE(self, timeperiod=20,
                     type='line', color='secondary', **kwargs):
    """Hilert Transform - Instantaneous Trendline."""

    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'HTTrendline'
    self.pri[name] = dict(type=type, color=color)
    self.ind[name] = talib.HT_TRENDLINE(self.df[self.cl].values)


# Momentum indicators


def add_RSI(self, timeperiod=14,
            type='line', color='secondary', **kwargs):
    """Relative Strength Index."""

    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'RSI({})'.format(str(timeperiod))
    self.sec[name] = dict(type=type, color=color)
    self.ind[name] = talib.RSI(self.df[self.cl].values, timeperiod)


def add_ADX(self, timeperiod=14,
            type='line', color='secondary', **kwargs):
    """Average Directional Movement Index."""

    if not (self.has_high and self.has_low and self.has_close):
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'ADX({})'.format(str(timeperiod))
    self.sec[name] = dict(type=type, color=color)
    self.ind[name] = talib.ADX(self.df[self.hi].values,
                               self.df[self.lo].values,
                               self.df[self.cl].values,
                               timeperiod)


def add_ADXR(self, timeperiod=14,
             type='line', color='secondary', **kwargs):
    """Average Directional Movement Index Rating."""

    if not (self.has_high and self.has_low and self.has_close):
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'ADXR({})'.format(str(timeperiod))
    self.sec[name] = dict(type=type, color=color)
    self.ind[name] = talib.ADXR(self.df[self.hi].values,
                                self.df[self.lo].values,
                                self.df[self.cl].values,
                                timeperiod)


def add_APO(self, fastperiod=12, slowperiod=26, matype=0,
            type='line', color='secondary', **kwargs):
    """Absolute Price Oscillator."""

    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'APO({}, {})'.format(str(fastperiod), str(slowperiod))
    self.sec[name] = dict(type=type, color=color)
    self.ind[name] = talib.ADXR(self.df[self.cl].values,
                                fastperiod, slowperiod, matype)


def add_AROON(self, timeperiod=14,
              types=['line', 'line'],
              colors=['increasing', 'decreasing'],
              **kwargs):
    """Aroon indicators.

    Note that the first argument of types and colors refers to Aroon up while
    the second argument refers to Aroon down.

    """
    if not (self.has_high and self.has_low):
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']
    if 'kinds' in kwargs:
        types = kwargs['type']

    if 'color' in kwargs:
        colors = [kwargs['color'], kwargs['color']]
    if 'type' in kwargs:
        types = [kwargs['type'], kwargs['type']]

    name = 'Aroon({})'.format(str(timeperiod))
    uaroon = name + '[Up]'
    daroon = name + '[Dn]'
    self.sec[uaroon] = dict(type=types[0], color=colors[0])
    self.sec[daroon] = dict(type=types[1], color=colors[1], on=uaroon)
    self.ind[uaroon], self.ind[daroon] = talib.AROON(self.df[self.hi].values,
                                                     self.df[self.lo].values,
                                                     timeperiod)
