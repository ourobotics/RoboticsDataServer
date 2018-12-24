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

# Premades
from time import time
import socket
import traceback
from threading import Thread
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
		self.connectionStatus = False
		self.connectionController = ConnectionController() 
		self.socketTimeout = 1
		self.addr = (None, None)
		self.threadWatch = None
		# ||=======================||
		socket.setdefaulttimeout(self.socketTimeout)
		self.listener = socket.socket()

	def jsonify(self, message = "Null", time = -1, function = "jsonify"):
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
				"Host": self.host,
				"Port": self.port,
				"Connection Status": self.connectionStatus,
				"Address": str(self.addr[0]) + ', ' + str(self.addr[1]),
				"Timeout": self.socketTimeout
			}
		}

	def buildListener(self):
		# ||=======================||
		WATCH = time()

		while True:
			try:
				self.listener.bind((self.host, self.port))
				print(self.host,self.port)
				break
			except Exception as e:
				# str(traceback.format_exc())
				self.port += 1

		message = "Server Created @: " + str(self.host) + ", Port: " + str(self.port)

		return self.jsonify(
			"Server Created @: " + str(self.host) + ", Port: " + str(self.port),
			time()-WATCH, 
			"buildListener"
		)

	def beginListenProtocal(self):
		# WATCH = time()
		# self.listener.listen(500)
		# self.active = True
		listenProtocalThread = Thread(target = self.listenProtocal)
		listenProtocalThread.setDaemon(True)
		listenProtocalThread.start()
		return self.jsonify(
			"Server Listening @: " + str(self.host) + ", Port: " + str(self.port),
			time()-WATCH, 
			"listen"
		)

	def networkServerThread(self):
		self.threadWatch = time()
		WATCH = time()
		self.active = True
		self.listener.listen(500)

		while self.active:
			if (self.connectionStatus == False):
				try:
					# print("Listening")
					conn, self.addr = self.listener.accept()
					print("Connection Created:","Address:",self.addr[0],"Port:",self.addr[1])
					self.connectionStatus = True
					self.connectionController.setConnection(conn, self.addr)
					self.connectionController.connectionCycle()
					self.connectionStatus = False
					conn.close()
				except socket.timeout as e:
					continue
				except Exception as e:
					print(e)
					return self.jsonify(
						"Failure In Accepting Connection(s)",
						time()-WATCH, 
						"listenProtocal"
					)

	def closeServer(self):
		WATCH = time()
		self.active = False
		sleep(0.1)
		self.listener.close()
		return self.jsonify(
			"Server Closed",
			time()-WATCH, 
			"closeServer"
		) 
		
# |===============================================================|