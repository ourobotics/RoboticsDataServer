# |===============================================================|
# ||
# ||  Program/File:		ConnectionController.py
# ||
# ||  Description:		
# ||
# ||  Author:           Logan Wilkovich
# ||  Email:            LWilkovich@gmail.com
# ||  Creation Date:	23 July 2018 | Logan Wilkovich
# |===============================================================|
# |===============================================================|
# ||=======================||
# Routes
# Controllers
# Tools
# Test
# Cache
from DeviceData import DeviceData
from EngineData import EngineData
# Premades
from time import time, strftime, localtime
from _thread import start_new_thread
import traceback
import socket
from ast import literal_eval
import pickle
# ||=======================||
# Global Variables

# ||=======================||
# Notes

# ||=======================||
# |===============================================================|

class ConnectionController(object):
	def __init__(self, conn = None, addr = (None, None)):
		self.type = "ConnectionController"
		self.active = True
		self.connection = conn
		self.address = addr

	def jsonify(self, message = "Null", time = strftime("%a;%d-%m-%Y;%H:%M:%S", localtime()), function = "Null"):
		return {
			"Generic Information": {
				"_Class": self.type,
				"_Function": function,
				"Return Status": True,
				"Activity": self.active,
				"Message": message,
				"Time": time 
			},
			"Specific Information": {
				"Address": str(self.address[0]) + ', ' + str(self.address[1])
			}
		}

	def updateCurrentDutyLog(self, duty, function = "updateCurrentDutyLog"):
		self.duty = duty
		DeviceData.ConnectionController.pushInternalLog(self.jsonify(
			"Duty Update: " + self.duty,
			str(strftime("%a;%d-%m-%Y;%H:%M:%S", localtime())),
			function)
		)
		return 0

	def updateCurrentDuty(self, duty):
		self.duty = duty
		return 0

	def createInteractionLog(self, data):
		return self.jsonify(
			str(data[1]),
			str(strftime("%a;%d-%m-%Y;%H:%M:%S", localtime())),
			"createInteractionLog"
		)

	def setConnection(self, conn, addr):
		self.updateCurrentDutyLog("Connection being set", "setConnection")
		self.connection = conn
		self.address = addr
		return 0


	def connectionCycle(self):
		self.updateCurrentDutyLog("Starting Connection Cycle", "connectionCycle")

		if (self.connection == None or self.address == None):
			self.active = False
			self.updateCurrentDutyLog("Invalid Connection Or Address", "connectionCycle")
			return 0
		
		while self.active:
			self.updateCurrentDuty("Listening")
			dataRecv = None
			try:
				dataRecv = self.connection.recv(1024).decode()
				# print(dataRecv)
				try:
					currentData = literal_eval(dataRecv)
				except Exception as e:
					dataRecv = None
				# print(currentData)
			except socket.timeout as e:
				continue
			except Exception as e:
				print(e)
				self.active = False
				self.updateCurrentDutyLog("Successfully Closing Thread -> readSocketCycle", "connectionCycle")
				return 0

			if (dataRecv != None):

				CODE = currentData[0]
				INFO = currentData[1]
				# print(currentData)

				# ||=======================||
				# Return Connection Success
				if (CODE == "#00000"):
					message = "Echo - Connection Successful"
					self.connection.send((message).encode())
					DeviceData.ConnectionController.pushInteractionLog(self.createInteractionLog(currentData))
					print(message)


				# ||=======================||
				# Test Server Connection
				elif (CODE == "#00001"):
					message = "Echo Connection Time Test"
					self.connection.send((message).encode())
					DeviceData.ConnectionController.pushInteractionLog(self.createInteractionLog(currentData))
					print(message)

				# ||=======================||
				# Write Data To DeviceData
				elif (CODE == "#00002"):
					message = "Success"
					self.connection.send((message).encode())
					# tmpData = dataRecv[7:]
					DeviceData.ConnectionController.pushInteractionLog(self.createInteractionLog(currentData))
					print("Device Data:", INFO)

				# ||=======================||
				# Set Gps Live Data
				elif (CODE == "#40001"):
					message = "Recieved Gps Controller Live Data"
					gpsControllerData = pickle.loads(currentData[1])
					EngineData.GpsController.setLiveData(gpsControllerData)
					DeviceData.ConnectionController.pushInteractionLog(self.createInteractionLog((currentData[0], message)))
					print(message)

				# ||=======================||
				# Push Gps Internal Log
				elif (CODE == "#40002"):
					continue

				# ||=======================||
				# Set Mechanical Live Data
				elif (CODE == "#40003"):
					message = "Recieved Mechanical Controller Live Data"
					mechanicalControllerData = pickle.loads(currentData[1])
					EngineData.MechanicalController.setLiveData(mechanicalControllerData)
					DeviceData.ConnectionController.pushInteractionLog(self.createInteractionLog((currentData[0], message)))
					print(message)

				# ||=======================||
				# Push Mechanical Internal Log
				elif (CODE == "#40004"):
					continue

				# ||=======================||
				# Set Thermo Live Data
				elif (CODE == "#40005"):
					message = "Recieved Thermo Controller Live Data"
					thermoControllerData = pickle.loads(currentData[1])
					EngineData.ThermoController.setLiveData(thermoControllerData)
					DeviceData.ConnectionController.pushInteractionLog(self.createInteractionLog((currentData[0], message)))
					print(message)
					
				# ||=======================||
				# Push Thermo Internal Log
				elif (CODE == "#40006"):
					continue

				# ||=======================||
				# Set Energy Live Data
				elif (CODE == "#40007"):
					message = "Recieved Energy Controller Live Data"
					energyControllerData = pickle.loads(currentData[1])
					EngineData.EnergyController.setLiveData(energyControllerData)
					DeviceData.ConnectionController.pushInteractionLog(self.createInteractionLog((currentData[0], message)))
					print(message)
					
				# ||=======================||
				# Push Energy Internal Log
				elif (CODE == "#40008"):
					continue

				# ||=======================||
				# Close Client Connection
				elif (CODE == "#99999"):
					self.connection.send(("Success").encode())
					return

				dataRecv = None

		return

# |===============================================================|