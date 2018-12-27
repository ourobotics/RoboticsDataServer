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
# |===============================================================|

class DeviceData:
    
    # |===============================================================|
    class ConnectionController:
        ConnectionController = {
            "LiveData": None,
            "InternalLog": [],
            "InteractionLog": []
        }

        # ||=======================||
        # LiveData Helpers  
        @classmethod
        def getLiveData(cls):
            return cls.ConnectionController["LiveData"]

        @classmethod
        def setLiveData(cls, data):
            cls.ConnectionController["LiveData"] = data

        # ||=======================||
        # InteractionLog Helpers
        @classmethod
        def pushInteractionLog(cls, data):
            cls.ConnectionController["InteractionLog"].append(data)

        @classmethod
        def getInteractionLog(cls, i):
            # print(i)
            if (i == None):
                return cls.ConnectionController["InteractionLog"]
            else:
                return cls.ConnectionController["InteractionLog"][int(i)]

        # ||=======================||
        # InternalLog Helpers
        @classmethod
        def pushInternalLog(cls, data):
            cls.ConnectionController["InternalLog"].append(data)

        @classmethod
        def getInternalLog(cls, i):
            # print(i)
            if (i == None):
                return cls.ConnectionController["InternalLog"]
            else:
                return cls.ConnectionController["InternalLog"][int(i)]

    # |===============================================================|
    class NetworkServer:
        NetworkServer = {
            "LiveData": None,
            "InternalLog": []
        }

        # ||=======================||
        # LiveData Helpers
        @classmethod
        def getLiveData(cls):
            return cls.NetworkServer["LiveData"]

        @classmethod
        def setLiveData(cls, data):
            cls.NetworkServer["LiveData"] = data

        # ||=======================||
        # InteralLog Helpers
        @classmethod
        def pushInternalLog(cls, data):
            cls.NetworkServer["InternalLog"].append(data)

        @classmethod
        def getInternalLog(cls, i):
            if (i == None):
                return cls.NetworkServer["InternalLog"]
            else:
                return cls.NetworkServer["InternalLog"][int(i)]

    # |============================================================================|