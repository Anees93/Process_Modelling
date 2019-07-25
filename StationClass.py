class Station(object):

    def __init__(self, pStaID=None, pStaIsIdle=None,
                 pStaMean=None, pStaSD=None,
                 pNextSta=None, pCapacity=None,
                 pServing=None):

        self.pStaID = pStaID
        self.pStaIsIdle = pStaIsIdle
        self.pStaMean = pStaMean
        self.pStaSD = pStaSD
        self.pNextSta = pNextSta
        self.pCapacity = pCapacity
        self.pServing = pServing

    def get_StaID(self):
        return self.pStaID

    def set_StaID(self, value):
        self.pStaID = value

    def get_StaIsIdle(self):
        return self.pStaIsIdle

    def set_StaIsIdle(self, value):
        self.pStaIsIdle = value

    def get_StaMean(self):
        return self.pStaMean

    def set_StaMean(self, value):
        self.pStaMean = value

    def get_StaSD(self):
        return self.pStaSD

    def set_StaSD(self, value):
        self.pStaSD = value

    def get_NextSta(self):
        return self.pNextSta

    def set_NextSta(self, value):
        self.pNextSta = value

    def get_Capacity(self):
        return self.pCapacity

    def set_Capacity(self, value):
        self.pCapacity = value

    def get_Serving(self):
        return self.pServing

    def set_Serving(self, value):
        self.pServing = value