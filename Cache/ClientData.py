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

class ClientData:

    @classmethod
    def getClientData(cls, type):
        return cls.jsonData

    @classmethod
    def setClientData(cls, type, data):
        cls.jsonData = data
        
# |===============================================================|