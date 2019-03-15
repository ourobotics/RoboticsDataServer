# |===============================================================|
# ||
# ||  Program/File:		ServerConnectionController.py
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
from ConnectionController import ConnectionController
# Tools
from ConfigLoader import ConfigLoader
from DebugLogger import DebugLogger
# Test
# Data
from DeviceData import DeviceData
# Premades
from time import sleep, time, strftime, localtime
import socket
import traceback
from threading import Thread
import ast
# ||=======================||
# Global Variables

# ||=======================||
# Notes

# ||=======================||
# |============================================================================|

class NetworkServer(object):
	def __init__(self):
		self.type = "NetworkServer"

		self.config = self.loadConfig(self.type)

		self.active = False
		
		# ||=======================||
		# Config <bool>
		self.debug = ast.literal_eval(self.config["Debug"])
		self.log = ast.literal_eval(self.config["Log"])

		# ||=======================||
		# Config <string>
		self.address = self.config[self.checkDebug() + "Address"]
		self.port = int(self.config[self.checkDebug() + "Port"])

		# ||=======================||
		# Defaults
		self.duty = "Inactive"
		self.connectionStatus = False
		self.connectionController = ConnectionController() 
		self.socketTimeout = 1
		self.addr = (None, None)
		socket.setdefaulttimeout(self.socketTimeout)
		self.listener = socket.socket()

		self.debugLogger = DebugLogger(self.type)
		self.debugLogger.setMessageSettings(
			ast.literal_eval(self.config["Debug"]),
			ast.literal_eval(self.config["Standard"]),
			ast.literal_eval(self.config["Warning"]),
			ast.literal_eval(self.config["Error"]))

	# |============================================================================|
	# |============================================================================|
	# |============================================================================|
	# |============================================================================|
	# |============================================================================|
	# |============================================================================|
	# |============================================================================|
	# |============================================================================|
	# |============================================================================|
	# |============================================================================|
	# |============================================================================|
	# |============================================================================|
	# |============================================================================|
	# |============================================================================|
	# |============================================================================|
	# |============================================================================|
	# |============================================================================|
	# |============================================================================|

	def loadConfig(self, configName):
		configLoader = ConfigLoader()
		config = configLoader.getConfig(configName)
		return config

	# |============================================================================|

	def checkDebug(self):
		if (self.debug == True):
			return "Debug"
		return ""

	# |============================================================================|

	def updateCurrentDutyLog(self, duty, function = "updateCurrentDutyLog"):
		self.duty = duty
		DeviceData.NetworkServer.pushInternalLog(self.jsonify(
			"Duty Update: " + self.duty,
			str(strftime("%a;%d-%m-%Y;%H:%M:%S", localtime())),
			function)
		)
		return 0

	# |============================================================================|

	def updateCurrentDuty(self, duty):
		self.duty = duty
		return 0

	# |============================================================================|
	# |============================================================================|
	# |============================================================================|
	# |============================================================================|
	# |============================================================================|
	# |============================================================================|
	# |============================================================================|
	# |============================================================================|
	# |============================================================================|
	# |============================================================================|
	# |============================================================================|
	# |============================================================================|
	# |============================================================================|
	# |============================================================================|
	# |============================================================================|
	# |============================================================================|
	# |============================================================================|
	# |============================================================================|

	def jsonify(self, message = "Null", time = strftime("%a;%d-%m-%Y;%H:%M:%S", localtime()), function = "Null"):
		return {
			"Generic Information": {
				"_Class": self.type,
				"_Function": function,
				"Duty": self.duty,
				"Return Status": True,
				"Activity": self.active,
				"Message": message,
				"Time": time
			},
			"Specific Information": {
				"Address": self.address,
				"Port": self.port,
				"Connection Status": self.connectionStatus,
				"Connected Address": str(self.addr[0]) + ', ' + str(self.addr[1]),
				"Timeout": self.socketTimeout,
				"Debug": self.debug,
				"Log": self.log
			}
		}

	# |============================================================================|

	def buildListener(self):
		# ||=======================||
		self.updateCurrentDutyLog("Building Listener" , "buildListener")

		while True:
			try:
				self.listener.bind((self.address, self.port))
				break
			except Exception as e:
			# ||=======================||
				logMessage = "Failure To Listen At Port " + str(self.port) + ": " + str(e) + " buildListener"
				self.debugLogger.log("Warning", logMessage)
				# ||=======================||
				self.port += 1

		message = "Server Created @: " + str(self.address) + ", Port: " + str(self.port)

		self.updateCurrentDutyLog("Server Created @: " + str(self.address) + ", Port: " + str(self.port), "buildListener")
		return 0

	# |============================================================================|

	def beginListenProtocal(self):
		self.updateCurrentDutyLog("Starting listenProtocalThread", "beginListenProtocal")
		listenProtocalThread = Thread(target = self.listenProtocal)
		listenProtocalThread.setDaemon(True)
		listenProtocalThread.start()
		
		self.updateCurrentDutyLog("Server Listening @: " + str(self.address) + ", Port: " + str(self.port), "buildListener")
		return 0

	# |============================================================================|

	def networkServerThread(self):
		self.updateCurrentDutyLog("networkServerThread Created")

		self.active = True
		self.listener.listen(500)

		self.updateCurrentDutyLog("Server Listening @: " + str(self.address) + ", Port: " + str(self.port), "networkServerThread")
		while self.active:
			self.updateCurrentDuty("Server Listening @: " + str(self.address) + ", Port: " + str(self.port))
			if (self.connectionStatus == False):
				try:
					conn, self.addr = self.listener.accept()

					# ||=======================||
					logMessage = "Connection Created: Address: " + str(self.addr[0]) + " Port: " + str(self.addr[1])
					self.debugLogger.log("Standard", logMessage)
					# ||=======================||

					self.connectionStatus = True
					self.connectionController.setConnection(conn, self.addr)
					self.updateCurrentDutyLog("ConnectionController Active", "networkServerThread")
					self.connectionController.connectionCycle()
					self.connectionStatus = False
					conn.close()
					self.updateCurrentDutyLog("ConnectionController Closed", "networkServerThread")
				except socket.timeout as e:
					# ||=======================||
					# logMessage = "Failure Socket Timed Out:" + str(e) + " networkServerThread"
					# self.debugLogger.log("Warning", logMessage)
					continue
					# ||=======================||
				# except Exception as e:
				# 	conn.close()
				# 	self.active = False
				# 	# ||=======================||
				# 	logMessage = "Failure In Accepting/Maintaining Connection(s): " + str(e) + " networkServerThread"
				# 	self.debugLogger.log("Error", logMessage)
				# 	# ||=======================||
				# 	return 0

	# |============================================================================|

	def closeServer(self):
		WATCH = time()
		self.active = False
		sleep(0.1)
		self.listener.close()
		self.updateCurrentDutyLog("Server Closed", "closeServer")
		# ||=======================||
		logMessage = "Server Closed"
		self.debugLogger.log("Standard", logMessage)
		# ||=======================||
		return 0
		
# |===============================================================|