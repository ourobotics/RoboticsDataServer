# ||===============================================================||
# ||
# ||  Program/File:     RoboticsDataServer.py
# ||
# ||  Description:		
# ||
# ||  Author:           Logan Wilkovich
# ||  Email:            LWilkovich@gmail.com
# ||  Creation Date:    21 November 2018 | Logan Wilkovich
# ||===============================================================||
# ||============================================================================||
# ||=======================||
# Routes
from Routes.Routes import Routes
# Server
from NetworkServer import NetworkServer
# Controllers
# from MicroControllerController import MicroControllerController
# from ServerConnectionController import ServerConnectionController
# from NetworkProtocalController import NetworkProtocalController
# from TimeDisplayController import TimeDisplayController
# from ApiController import ApiController
# Tools
# from LoggingTool import LoggingTool
# from ExitStatusParserTool import ExitStatusParserTool
# from PropertyLoaderTool import PropertyLoaderTool
# from BoolObjectCheckerTool import boolObjectChecker
# Test
# from TestSuite import TestSuite
# Premades
# from threading import Thread
# from time import strftime, localtime, sleep, time
# from ast import literal_eval
# import queue
import traceback
# ||=======================||
# Global Variables

# ||=======================||
# Notes

# ||=======================||
# ||============================================================================||

class RoboticsDataServer(object):
	def __init__(self):
		# ||=======================||
		# Program Classes
		self.networkServer = NetworkServer()
		

		# ||=======================||
		# Program Setup
		if True:
			self.networkServer.buildListener()
			self.networkServer.listen()

		try:
			while True:
				continue
		except KeyboardInterrupt as e:
			str(traceback.format_exc())
			return

rds = RoboticsDataServer()