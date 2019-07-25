class Customer(object):

    def __init__(self, pCustID=None, pIsIdle=None,
                 pStation=None, pIdleTime=None,
                 pStartTime=None, pEndTime=None,
                 pNextSta=None, pEntered=None,
                 pLeft=None):

        self.pCustID = pCustID
        self.pIsIdle = pIsIdle
        self.pStation = pStation
        self.pIdleTime = pIdleTime
        self.pStartTime = pStartTime
        self.pEndTime = pEndTime
        self.pNextSta = pNextSta
        self.pEntered = pEntered
        self.pLeft = pLeft


    def get_CustID(self):
        return self.pCustID

    def set_CustID(self, value):
        self.pCustID = value

    def get_IsIdle(self):
        return self.pIsIdle

    def set_IsIdle(self, value):
        self.pIsIdle = value

    def get_Station(self):
        return self.pStation

    def set_Station(self, value):
        self.pStation = value

    def get_IdleTime(self):
        return self.pIdleTime

    def set_IdleTime(self, value):
        self.pIdleTime = value

    def get_StartTime(self):
        return self.pStartTime

    def set_StartTime(self, value):
        self.pStartTime = value

    def get_EndTime(self):
        return self.pEndTime

    def set_EndTime(self, value):
        self.pEndTime = value

    def get_NextSta(self):
        return self.pNextSta

    def set_NextSta(self, value):
        self.pNextSta = value

    def get_Entered(self):
        return self.pEntered

    def set_Entered(self, value):
        self.pEntered = value

    def get_Left(self):
        return self.pLeft

    def set_Left(self, value):
        self.pLeft = value