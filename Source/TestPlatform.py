# ||==============================================================||
# ||
# ||  Program/File:     TestPlatform.py
# ||
# ||  Description:		
# ||
# ||  Author:           Logan Wilkovich
# ||  Email:            LWilkovich@gmail.com
# ||  Creation Date:    21 November 2018 | Logan Wilkovich
# ||===============================================================||
# ||===============================================================||
# ||=======================||
# Routes
from System.Routes import Routes
# Server
from NetworkServer import NetworkServer
from FlaskServer import FlaskServer
# Controllers
# Tools
from DebugLogger import DebugLogger
from ConfigLoader import ConfigLoader
# Test
# Data
from DeviceData import DeviceData
# Premades
from threading import Thread
from time import sleep, time, strftime, localtime
import traceback
import sys
# ||=======================||
# Global Variables

# ||=======================||
# Notes

# ||=======================||
# ||===============================================================||

class RoboticsDataServer(object):
	def __init__(self):
		# ||=======================||
		# Program Config Varaibles
		self.useNetworkServer = True
		self.useFlaskServer = True
		self.useApiService = True

		# ||=======================||
		# Program Classes
		self.networkServer = NetworkServer()
		self.flaskServer = FlaskServer(self.useApiService)

	def main(self):
		# ||=======================||
		configLoader = ConfigLoader()
		config = configLoader.getConfig("FlaskServer")
		print(config["Address"])
		print(self.networkServer.jsonify())
		print(sys.getsizeof(self.networkServer.jsonify()))

		self.debugLogger = DebugLogger("Main")
		self.debugLogger.setMessageSettings(True, True, True)
		for i in range(650):
			# print(i)
			self.debugLogger.log("Warning", "Hello World "+str(i))
		# self.debugLogger.dumpMessageBuffer()


rds = RoboticsDataServer()
rds.main()

# |===============================================================|