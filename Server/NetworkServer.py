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
# Test
# Data
from DeviceData import DeviceData
# Premades
from time import sleep, time, strftime, localtime
import socket
import traceback
from threading import Thread
from ast import literal_eval
# ||=======================||
# Global Variables

# ||=======================||
# Notes

# ||=======================||
# |============================================================================|

class NetworkServer(object):
	def __init__(self):
		self.active = False
		self.type = "NetworkServer"
		self.host = ""
		self.port = 1024
		self.duty = "Inactive"
		self.connectionStatus = False
		self.connectionController = ConnectionController() 
		self.socketTimeout = 1
		self.addr = (None, None)
		# ||=======================||
		socket.setdefaulttimeout(self.socketTimeout)
		self.listener = socket.socket()

	def jsonify(self, message = "Null", time = -1, function = "jsonify"):
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
				"Host": self.host,
				"Port": self.port,
				"Connection Status": self.connectionStatus,
				"Address": str(self.addr[0]) + ', ' + str(self.addr[1]),
				"Timeout": self.socketTimeout
			}
		}

	def updateCurrentDutyLog(self, duty, function = "updateCurrentDutyLog"):
		self.duty = duty
		DeviceData.NetworkServer.pushInternalLog(self.jsonify(
			"Duty Update: " + self.duty,
			str(strftime("%Y-%m-%d %H:%M:%S", localtime())),
			function)
		)

	def updateCurrentDuty(self, duty):
		self.duty = duty
		return 0

	def buildListener(self):
		# ||=======================||
		WATCH = time()
		self.updateCurrentDutyLog("Building Listener")

		while True:
			try:
				self.listener.bind((self.host, self.port))
				print(self.host,self.port)
				break
			except Exception as e:
				# str(traceback.format_exc())
				self.port += 1

		message = "Server Created @: " + str(self.host) + ", Port: " + str(self.port)

		self.updateCurrentDutyLog("Server Created @: " + str(self.host) + ", Port: " + str(self.port), "buildListener")
		return 0

	def beginListenProtocal(self):
		self.updateCurrentDutyLog("Starting listenProtocalThread", "beginListenProtocal")
		# self.listener.listen(500)
		# self.active = True
		listenProtocalThread = Thread(target = self.listenProtocal)
		listenProtocalThread.setDaemon(True)
		listenProtocalThread.start()
		
		self.updateCurrentDutyLog("Server Listening @: " + str(self.host) + ", Port: " + str(self.port), "buildListener")
		return 0

	def networkServerThread(self):
		self.updateCurrentDutyLog("networkServerThread Created")

		self.active = True
		self.listener.listen(500)

		self.updateCurrentDutyLog("Listening")
		while self.active:
			self.updateCurrentDuty("Listening")
			if (self.connectionStatus == False):
				try:
					conn, self.addr = self.listener.accept()
					print("Connection Created:","Address:",self.addr[0],"Port:",self.addr[1])
					self.connectionStatus = True
					self.connectionController.setConnection(conn, self.addr)
					self.updateCurrentDutyLog("ConnectionController Active")
					self.connectionController.connectionCycle()
					self.connectionStatus = False
					conn.close()
					self.updateCurrentDutyLog("ConnectionController Closed")
				except socket.timeout as e:
					continue
				except Exception as e:
					self.updateCurrentDutyLog("Failure In Accepting/Maintaining Connection(s):" + e, "networkServerThread")
					return 0

	def closeServer(self):
		WATCH = time()
		self.active = False
		sleep(0.1)
		self.listener.close()
		self.updateCurrentDutyLog("Server Closed", "closeServer")
		return 0
		
# |===============================================================|