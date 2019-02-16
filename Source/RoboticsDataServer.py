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
import json
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

		# ||=======================||
		# Program Classes
		self.networkServer = NetworkServer()
		self.flaskServer = FlaskServer()

		# ||=======================||
		# Display Program Classes Configs
		print("Display Program Classes Configs:")
		print("Flask Server Configuration:",(self.flaskServer.jsonify("Printing Configuration")["Specific Information"]))
		print("Network Server Configuration:",(self.networkServer.jsonify("Printing Configuration")["Specific Information"]))
		print()

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
				# data = DeviceData.getLiveDeviceData()
				
				networkServerData = self.networkServer.jsonify(
					"Requesting Current Cache", 
					str(strftime("%a;%d-%m-%Y;%H:%M:%S", localtime())))
				connectionControllerData = self.networkServer.connectionController.jsonify(
					"Requesting Current Cache", 
					str(strftime("%a;%d-%m-%Y;%H:%M:%S", localtime())))

				DeviceData.NetworkServer.setLiveData(networkServerData)
				DeviceData.ConnectionController.setLiveData(connectionControllerData)
				# DeviceData.setLiveDeviceData(data)

		except KeyboardInterrupt as e:
			# print(str(traceback.format_exc()))
			return

rds = RoboticsDataServer()
rds.main()

# |===============================================================|