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
    """Moving Average (customizable)."""

    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'MA({})'.format(str(timeperiod))
    self.pri[name] = dict(type=type, color=color)
    self.ind[name] = talib.MA(self.df[self.cl].values,
                              timeperiod, matype)


def add_SMA(self, timeperiod=20,
            type='line', color='secondary', **kwargs):
    """Simple Moving Average."""

    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'SMA({})'.format(str(timeperiod))
    self.pri[name] = dict(type=type, color=color)
    self.ind[name] = talib.SMA(self.df[self.cl].values,
                               timeperiod)


def add_EMA(self, timeperiod=26,
            type='line', color='secondary', **kwargs):
    """Exponential Moving Average."""

    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'EMA({})'.format(str(timeperiod))
    self.pri[name] = dict(type=type, color=color)
    self.ind[name] = talib.EMA(self.df[self.cl].values,
                               timeperiod)


def add_WMA(self, timeperiod=20,
            type='line', color='secondary', **kwargs):
    """Weighted Moving Average."""

    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'WMA({})'.format(str(timeperiod))
    self.pri[name] = dict(type=type, color=color)
    self.ind[name] = talib.WMA(self.df[self.cl].values,
                               timeperiod)


def add_DEMA(self, timeperiod=26,
             type='line', color='secondary', **kwargs):
    """Double Exponential Moving Average."""

    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'DEMA({})'.format(str(timeperiod))
    self.pri[name] = dict(type=type, color=color)
    self.ind[name] = talib.DEMA(self.df[self.cl].values,
                                timeperiod)


def add_TEMA(self, timeperiod=26,
             type='line', color='secondary', **kwargs):
    """Triple Moving Exponential Average."""

    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'TEMA({})'.format(str(timeperiod))
    self.pri[name] = dict(type=type, color=color)
    self.ind[name] = talib.TEMA(self.df[self.cl].values,
                                timeperiod)


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
    self.ind[name] = talib.T3(self.df[self.cl].values,
                              timeperiod, vfactor)


def add_KAMA(self, timeperiod=20,
             type='line', color='secondary', **kwargs):
    """Kaufmann Adaptive Moving Average."""

    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'KAMA({})'.format(str(timeperiod))
    self.pri[name] = dict(type=type, color=color)
    self.ind[name] = talib.KAMA(self.df[self.cl].values,
                                timeperiod)


def add_TRIMA(self, timeperiod=20,
              type='line', color='secondary', **kwargs):
    """Triangular Moving Average."""

    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'TRIMA({})'.format(str(timeperiod))
    self.pri[name] = dict(type=type, color=color)
    self.ind[name] = talib.TRIMA(self.df[self.cl].values,
                                 timeperiod)


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

    if 'type' in kwargs:
        types = [kwargs['type']] * 2
    if 'color' in kwargs:
        colors = [kwargs['color']] * 2

    mama = 'MAMA({},{})'.format(str(fastlimit), str(slowlimit))
    fama = 'FAMA({},{})'.format(str(fastlimit), str(slowlimit))
    self.pri[mama] = dict(type=types[0], color=colors[0])
    self.pri[fama] = dict(type=types[1], color=colors[1])
    self.ind[mama], self.ind[fama] = talib.MAMA(self.df[self.cl].values,
                                                fastlimit, slowlimit)


def add_MAVP(self, periods, minperiod=2, maxperiod=30, matype=0,
             type='line', color='secondary', **kwargs):
    """Moving Average with Variable Period.

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

    name = 'MAVP({},{})'.format(str(minperiod), str(maxperiod))
    self.pri[name] = dict(type=type, color=color)
    self.ind[name] = talib.MAVP(self.df[self.cl].values,
                                periods, minperiod, maxperiod, matype)


def add_BBANDS(self, timeperiod=20, nbdevup=2, nbdevdn=2, matype=0,
               types=['line_dashed_thin', 'line_dashed_thin'],
               colors=['tertiary', 'grey_strong'], **kwargs):
    """Bollinger Bands.

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

    if 'type' in kwargs:
        types = [kwargs['type']] * 2
    if 'color' in kwargs:
        colors = [kwargs['color']] * 2

    name = 'BBANDS({},{},{})'.format(str(timeperiod),
                                     str(nbdevup),
                                     str(nbdevdn))
    ubb = name + '[Upper]'
    bb = name
    lbb = name + '[Lower]'
    self.pri[ubb] = dict(type='line_' + types[0][5:],
                         color=colors[0])
    self.pri[bb] = dict(type='area_' + types[1][5:],
                        color=colors[1], fillcolor='fill')
    self.pri[lbb] = dict(type='area_' + types[0][5:],
                         color=colors[0], fillcolor='fill')
    (self.ind[ubb],
     self.ind[bb],
     self.ind[lbb]) = talib.BBANDS(self.df[self.cl].values,
                                   timeperiod, nbdevup, nbdevdn, matype)


def add_HT_TRENDLINE(self,
                     type='line', color='secondary', **kwargs):
    """Hilert Transform Instantaneous Trendline."""

    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'HT_TRENDLINE'
    self.pri[name] = dict(type=type, color=color)
    self.ind[name] = talib.HT_TRENDLINE(self.df[self.cl].values)


def add_MIDPOINT(self, timeperiod=14,
                 type='line', color='secondary', **kwargs):
    """Midpoint Price over Period."""

    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'MIDPOINT({})'.format(str(timeperiod))
    self.pri[name] = dict(type=type, color=color)
    self.ind[name] = talib.MIDPOINT(self.df[self.cl].values)


def add_SAR(self, acceleration=0.02, maximum=0.20,
            type='scatter', color='tertiary', **kwargs):
    """Parabolic SAR."""

    if not (self.has_high and self.has_low):
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'SAR({},{})'.format(str(acceleration), str(maximum))
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

    name = ('SAREXT({},{},{},{},'
            '{},{},{},{})'.format(str(startvalue), str(offsetonreverse),
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


# Momentum indicators


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
    self.ind[name] = talib.APO(self.df[self.cl].values,
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
        kwargs['type'] = kwargs['kind']
    if 'kinds' in kwargs:
        types = kwargs['type']

    if 'type' in kwargs:
        types = [kwargs['type']] * 2
    if 'color' in kwargs:
        colors = [kwargs['color']] * 2

    name = 'AROON({})'.format(str(timeperiod))
    uaroon = name + ' [Up]'
    daroon = name + ' [Dn]'
    self.sec[uaroon] = dict(type=types[0], color=colors[0])
    self.sec[daroon] = dict(type=types[1], color=colors[1], on=uaroon)
    self.ind[uaroon], self.ind[daroon] = talib.AROON(self.df[self.hi].values,
                                                     self.df[self.lo].values,
                                                     timeperiod)


def add_AROONOSC(self, timeperiod=14,
                 type='area', color='secondary', **kwargs):
    """Aroon Oscillator."""

    if not (self.has_high and self.has_low):
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'AROONOSC({})'.format(str(timeperiod))
    self.sec[name] = dict(type=type, color=color)
    self.ind[name] = talib.AROONOSC(self.df[self.hi].values,
                                    self.df[self.lo].values,
                                    timeperiod)


def add_BOP(self,
            type='histogram', color='tertiary', **kwargs):
    """Balance of Power."""

    if not self.has_OHLC:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'BOP'
    self.sec[name] = dict(type=type, color=color)
    self.ind[name] = talib.BOP(self.df[self.op].values,
                               self.df[self.hi].values,
                               self.df[self.lo].values,
                               self.df[self.cl].values)


def add_CCI(self, timeperiod=14,
            type='line', color='secondary', **kwargs):
    """Channel Commodity Index."""

    if not (self.has_high and self.has_low and self.has_close):
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'CCI({})'.format(str(timeperiod))
    self.sec[name] = dict(type=type, color=color)
    self.ind[name] = talib.CCI(self.df[self.hi].values,
                               self.df[self.lo].values,
                               self.df[self.cl].values,
                               timeperiod)


def add_CMO(self, timeperiod=14,
            type='line', color='secondary', **kwargs):
    """Chande Momentum Indicator."""

    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'CMO({})'.format(str(timeperiod))
    self.sec[name] = dict(type=type, color=color)
    self.ind[name] = talib.CMO(self.df[self.cl].values,
                               timeperiod)


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


def add_DX(self, timeperiod=14,
           type='line', color='secondary', **kwargs):
    """Directional Movement Index."""

    if not (self.has_high and self.has_low and self.has_close):
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'DX({})'.format(str(timeperiod))
    self.sec[name] = dict(type=type, color=color)
    self.ind[name] = talib.DX(self.df[self.hi].values,
                              self.df[self.lo].values,
                              self.df[self.cl].values,
                              timeperiod)


def add_MINUS_DI(self, timeperiod=14,
                 type='line', color='decreasing', **kwargs):
    """Minus Directional Indicator."""

    if not (self.has_high and self.has_low and self.has_close):
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'MINUS_DI({})'.format(str(timeperiod))
    self.sec[name] = dict(type=type, color=color)
    self.ind[name] = talib.MINUS_DI(self.df[self.hi].values,
                                    self.df[self.lo].values,
                                    self.df[self.cl].values,
                                    timeperiod)


def add_PLUS_DI(self, timeperiod=14,
                type='line', color='increasing', **kwargs):
    """Plus Directional Indicator."""

    if not (self.has_high and self.has_low and self.has_close):
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'PLUS_DI({})'.format(str(timeperiod))
    self.sec[name] = dict(type=type, color=color)
    self.ind[name] = talib.PLUS_DI(self.df[self.hi].values,
                                   self.df[self.lo].values,
                                   self.df[self.cl].values,
                                   timeperiod)


def add_MINUS_DM(self, timeperiod=14,
                 type='line', color='decreasing', **kwargs):
    """Minus Directional Movement."""

    if not (self.has_high and self.has_low):
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'MINUS_DM({})'.format(str(timeperiod))
    self.sec[name] = dict(type=type, color=color)
    self.ind[name] = talib.MINUS_DM(self.df[self.hi].values,
                                    self.df[self.lo].values,
                                    timeperiod)


def add_PLUS_DM(self, timeperiod=14,
                type='line', color='increasing', **kwargs):
    """Plus Directional Movement."""

    if not (self.has_high and self.has_low):
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'PLUS_DM({})'.format(str(timeperiod))
    self.sec[name] = dict(type=type, color=color)
    self.ind[name] = talib.PLUS_DM(self.df[self.hi].values,
                                   self.df[self.lo].values,
                                   timeperiod)


def add_MACD(self, fastperiod=12, slowperiod=26, signalperiod=9,
             types=['line', 'line', 'histogram'],
             colors=['primary', 'tertiary', 'fill'],
             **kwargs):
    """Moving Average Convergence Divergence.

    Note that the first argument of types and colors refers to MACD,
    the second argument refers to MACD signal line and the third argument
    refers to MACD histogram.

    """
    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        kwargs['type'] = kwargs['kind']
    if 'kinds' in kwargs:
        types = kwargs['type']

    if 'type' in kwargs:
        types = [kwargs['type']] * 3
    if 'color' in kwargs:
        colors = [kwargs['color']] * 3

    name = 'MACD({},{},{})'.format(str(fastperiod),
                                   str(slowperiod),
                                   str(signalperiod))
    macd = name
    smacd = name + '[Sign]'
    hmacd = name + '[Hist]'
    self.sec[macd] = dict(type=types[0], color=colors[0])
    self.sec[smacd] = dict(type=types[1], color=colors[1], on=macd)
    self.sec[hmacd] = dict(type=types[2], color=colors[2], on=macd)
    (self.ind[macd],
     self.ind[smacd],
     self.ind[hmacd]) = talib.MACD(self.df[self.cl].values,
                                   fastperiod, slowperiod,
                                   signalperiod)


def add_MACDEXT(self, fastperiod=12, fastmatype=0,
                slowperiod=26, slowmatype=0,
                signalperiod=9, signalmatype=0,
                types=['line', 'line', 'histogram'],
                colors=['primary', 'tertiary', 'fill'],
                **kwargs):
    """Moving Average Convergence Divergence with Controllable MA Type.

    Note that the first argument of types and colors refers to MACD,
    the second argument refers to MACD signal line and the third argument
    refers to MACD histogram.

    """
    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        kwargs['type'] = kwargs['kind']
    if 'kinds' in kwargs:
        types = kwargs['type']

    if 'type' in kwargs:
        types = [kwargs['type']] * 3
    if 'color' in kwargs:
        colors = [kwargs['color']] * 3

    name = 'MACDEXT({},{},{})'.format(str(fastperiod),
                                      str(slowperiod),
                                      str(signalperiod))
    macd = name
    smacd = name + '[Sign]'
    hmacd = name + '[Hist]'
    self.sec[macd] = dict(type=types[0], color=colors[0])
    self.sec[smacd] = dict(type=types[1], color=colors[1], on=macd)
    self.sec[hmacd] = dict(type=types[2], color=colors[2], on=macd)
    (self.ind[macd],
     self.ind[smacd],
     self.ind[hmacd]) = talib.MACDEXT(self.df[self.cl].values,
                                      fastperiod, fastmatype,
                                      slowperiod, slowmatype,
                                      signalperiod, signalmatype)


def add_MFI(self, timeperiod=14,
            type='line', color='secondary', **kwargs):
    """Money Flow Index."""

    if not (self.has_high and self.has_low and
            self.has_close and self.has_volume):
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'MFI({})'.format(str(timeperiod))
    self.sec[name] = dict(type=type, color=color)
    self.ind[name] = talib.MFI(self.df[self.hi].values,
                               self.df[self.lo].values,
                               self.df[self.cl].values,
                               self.df[self.vo].values,
                               timeperiod)


def add_MOM(self, timeperiod=10,
            type='line', color='secondary', **kwargs):
    """Momentum Indicator."""

    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'MOM({})'.format(str(timeperiod))
    self.sec[name] = dict(type=type, color=color)
    self.ind[name] = talib.MOM(self.df[self.cl].values,
                               timeperiod)


def add_PPO(self, fastperiod=12, slowperiod=26, matype=0,
            type='line', color='secondary',
            **kwargs):
    """Percent Price Oscillator."""

    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        kwargs['type'] = kwargs['kind']

    name = 'PPO({},{})'.format(str(fastperiod), str(slowperiod))
    self.ind[name] = talib.PPO(self.df[self.cl].values,
                               fastperiod, slowperiod,
                               matype)


def add_ROC(self, timeperiod=10,
            type='line', color='tertiary', **kwargs):
    """Rate of Change."""

    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'ROC({})'.format(str(timeperiod))
    self.sec[name] = dict(type=type, color=color)
    self.ind[name] = talib.ROC(self.df[self.cl].values,
                               timeperiod)


def add_ROCP(self, timeperiod=10,
             type='line', color='tertiary', **kwargs):
    """Rate of Change (Percentage)."""

    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'ROCP({})'.format(str(timeperiod))
    self.sec[name] = dict(type=type, color=color)
    self.ind[name] = talib.ROCP(self.df[self.cl].values,
                                timeperiod)


def add_ROCR(self, timeperiod=10,
             type='line', color='tertiary', **kwargs):
    """Rate of Change (Ratio)."""

    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'ROCR({})'.format(str(timeperiod))
    self.sec[name] = dict(type=type, color=color)
    self.ind[name] = talib.ROCR(self.df[self.cl].values,
                                timeperiod)


def add_ROCR100(self, timeperiod=10,
                type='line', color='tertiary', **kwargs):
    """Rate of Change (Ratio * 100)."""

    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'ROCR100({})'.format(str(timeperiod))
    self.sec[name] = dict(type=type, color=color)
    self.ind[name] = talib.ROCR100(self.df[self.cl].values,
                                   timeperiod)


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
    self.ind[name] = talib.RSI(self.df[self.cl].values,
                               timeperiod)


def add_STOCH(self, fastk_period=5, slowk_period=3,
              slowk_matype=0, slowd_period=3, slowd_matype=0,
              types=['line', 'line'],
              colors=['primary', 'tertiary'],
              **kwargs):
    """Slow Stochastic Oscillator.

    Note that the first argument of types and colors refers to Slow Stoch %K,
    while second argument refers to Slow Stoch %D
    (signal line of %K obtained by MA).

    """
    if not (self.has_high and self.has_low and self.has_close):
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        kwargs['type'] = kwargs['kind']
    if 'kinds' in kwargs:
        types = kwargs['type']

    if 'type' in kwargs:
        types = [kwargs['type']] * 2
    if 'color' in kwargs:
        colors = [kwargs['color']] * 2

    name = 'STOCH({},{},{})'.format(str(fastk_period),
                                    str(slowk_period),
                                    str(slowd_period))
    slowk = name + r'[%k]'
    slowd = name + r'[%d]'
    self.sec[slowk] = dict(type=types[0], color=colors[0])
    self.sec[slowd] = dict(type=types[1], color=colors[1], on=slowk)
    self.ind[slowk], self.ind[slowd] = talib.STOCH(self.df[self.hi].values,
                                                   self.df[self.lo].values,
                                                   self.df[self.cl].values,
                                                   fastk_period, slowk_period,
                                                   slowk_matype, slowd_period,
                                                   slowd_matype)


def add_STOCHF(self, fastk_period=5, fastd_period=3, fastd_matype=0,
               types=['line', 'line'],
               colors=['primary', 'tertiary'],
               **kwargs):
    """Fast Stochastic Oscillator.

    Note that the first argument of types and colors refers to Fast Stoch %K,
    while second argument refers to Fast Stoch %D
    (signal line of %K obtained by MA).

    """
    if not (self.has_high and self.has_low and self.has_close):
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        kwargs['type'] = kwargs['kind']
    if 'kinds' in kwargs:
        types = kwargs['type']

    if 'type' in kwargs:
        types = [kwargs['type']] * 2
    if 'color' in kwargs:
        colors = [kwargs['color']] * 2

    name = 'STOCHF({},{})'.format(str(fastk_period),
                                  str(fastd_period))
    fastk = name + r'[%k]'
    fastd = name + r'[%d]'
    self.sec[fastk] = dict(type=types[0], color=colors[0])
    self.sec[fastd] = dict(type=types[1], color=colors[1], on=fastk)
    self.ind[fastk], self.ind[fastd] = talib.STOCHF(self.df[self.hi].values,
                                                    self.df[self.lo].values,
                                                    self.df[self.cl].values,
                                                    fastk_period, fastd_period,
                                                    fastd_matype)


def add_STOCHRSI(self, timeperiod=14,
                 fastk_period=5, fastd_period=3, fastd_matype=0,
                 types=['line', 'line'],
                 colors=['primary', 'tertiary'],
                 **kwargs):
    """Stochastic Relative Strength Index.

    Note that the first argument of types and colors refers to StochRSI %K
    while second argument refers to StochRSI %D
    (signal line of %K obtained by MA).

    """
    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        kwargs['type'] = kwargs['kind']
    if 'kinds' in kwargs:
        types = kwargs['type']

    if 'type' in kwargs:
        types = [kwargs['type']] * 2
    if 'color' in kwargs:
        colors = [kwargs['color']] * 2

    name = 'STOCHRSI({},{},{})'.format(str(timeperiod),
                                       str(fastk_period),
                                       str(fastd_period))
    fastk = name + r'[%k]'
    fastd = name + r'[%d]'
    self.sec[fastk] = dict(type=types[0], color=colors[0])
    self.sec[fastd] = dict(type=types[1], color=colors[1], on=fastk)
    self.ind[fastk], self.ind[fastd] = talib.STOCHRSI(self.df[self.cl].values,
                                                      timeperiod,
                                                      fastk_period,
                                                      fastd_period,
                                                      fastd_matype)


def add_TRIX(self, timeperiod=15,
             type='area', color='secondary', **kwargs):
    """1-day Rate of Change of Triple Smooth EMA."""

    if not self.has_close:
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'TRIX({})'.format(str(timeperiod))
    self.sec[name] = dict(type=type, color=color)
    self.ind[name] = talib.TRIX(self.df[self.cl].values,
                                timeperiod)


def add_ULTOSC(self, timeperiod=14, timeperiod2=14, timeperiod3=28,
               type='line', color='secondary', **kwargs):
    """Ultimate Oscillator."""

    if not (self.has_high and self.has_low and self.has_close):
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'ULTOSC({})'.format(str(timeperiod),
                               str(timeperiod2),
                               str(timeperiod3))
    self.sec[name] = dict(type=type, color=color)
    self.ind[name] = talib.ULTOSC(self.df[self.hi].values,
                                  self.df[self.lo].values,
                                  self.df[self.cl].values,
                                  timeperiod,
                                  timeperiod2,
                                  timeperiod3)


def add_WILLR(self, timeperiod=14,
              type='line', color='secondary', **kwargs):
    """Williams %R."""

    if not (self.has_high and self.has_low and self.has_close):
        raise Exception()

    utils.kwargs_check(kwargs, VALID_TA_KWARGS)
    if 'kind' in kwargs:
        type = kwargs['kind']

    name = 'WILLR({})'.format(str(timeperiod))
    self.sec[name] = dict(type=type, color=color)
    self.ind[name] = talib.WILLR(self.df[self.hi].values,
                                 self.df[self.lo].values,
                                 self.df[self.cl].values,
                                 timeperiod)
