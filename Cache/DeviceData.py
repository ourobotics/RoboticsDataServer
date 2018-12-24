# |===============================================================|
# ||
# ||  Program/File:		DeviceData.py
# ||
# ||  Description:		Singleton To Represent Current Data Model
# ||
# ||  Author:           Logan Wilkovich
# ||  Email:            LWilkovich@gmail.com
# ||  Creation Date:	21 November 2018 | Logan Wilkovich
# |===============================================================|
# ||=======================||
# Routes
# Controllers

# Tools

# Test

# Premades
from time import time
import traceback
# ||=======================||
# Global Variables

# ||=======================||
# Notes

# ||=======================||
# |============================================================================|

class DeviceData:
    
    # |============================================================================|
    liveJsonData = {
        "NetworkServer": None,
        "ConnectionController": None
    }
    
    @classmethod
    def getLiveDeviceData(cls):
        return cls.liveJsonData

    @classmethod
    def setLiveDeviceData(cls, data):
        cls.liveJsonData = data
    # |============================================================================|

    ConnectionController = {
        "InteractionLog": []
    }

    @classmethod
    def appendInteractionLog(cls, data):
        cls.ConnectionController["InteractionLog"].append(data)

    @classmethod
    def getInteractionLog(cls, i):
        print(i)
        if (i == None):
            return cls.ConnectionController["InteractionLog"]
        else:
            return cls.ConnectionController["InteractionLog"][int(i)]

    # |============================================================================|

