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
from ConfigLoader import ConfigLoader
# Test
# Data
from DeviceData import DeviceData
# Premades
from threading import Thread
from time import sleep, time, strftime, localtime
import traceback
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

rds = RoboticsDataServer()
rds.main()

# |===============================================================|