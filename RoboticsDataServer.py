# ||==============================================================||
# ||
# ||  Program/File:     RoboticsDataServer.py
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
		# Program Setup
		if self.useNetworkServer:
			self.networkServer.buildListener()
			self.networkServerThread = Thread(target = self.networkServer.networkServerThread)
			self.networkServerThread.setDaemon(True)
			self.networkServerThread.start()
		if self.useFlaskServer:
			self.flaskServerThread = Thread(target = self.flaskServer.FlaskServerThread)
			self.flaskServerThread.setDaemon(True)
			self.flaskServerThread.start()
			
		sleep(1)
		try:
			while True:
				# continue
				sleep(1)
				data = DeviceData.getLiveDeviceData()
				
				data["NetworkServer"] = self.networkServer.jsonify(
					"Requesting Current Cache", 
					str(strftime("%Y-%m-%d %H:%M:%S", localtime())))
				data["ConnectionController"] = self.networkServer.connectionController.jsonify(
					"Requesting Current Cache", 
					str(strftime("%Y-%m-%d %H:%M:%S", localtime())))

				DeviceData.setLiveDeviceData(data)

		except KeyboardInterrupt as e:
			print(str(traceback.format_exc()))
			return

rds = RoboticsDataServer()
rds.main()

# |===============================================================|