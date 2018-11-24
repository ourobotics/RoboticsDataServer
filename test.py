class DeviceData:

    someJsonData = 50

    @classmethod
    def getDeviceData(cls):
        return cls.someJsonData

    @classmethod
    def setDeviceData(cls, data):
        cls.someJsonData = data
