def _MA(self, timeperiod=30):
    name = 'MA({})'.format(str(timeperiod))
    self.primary[name] = talib.MA(self.df[self.cl].values, timeperiod)

def _SMA(self, timeperiod=30):
    name = 'SMA({})'.format(str(timeperiod))
    self.primary[name] = talib.SMA(self.df[self.cl].values, timeperiod)

def _EMA(self, timeperiod=30):
    name = 'EMA({})'.format(str(timeperiod))
    self.primary[name] = talib.EMA(self.df[self.cl].values, timeperiod)
