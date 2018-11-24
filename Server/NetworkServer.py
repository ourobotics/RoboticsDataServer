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
		self.host = "localhost"
		self.port = 1024
		self.connectionStatus = False
		self.connectionController = ConnectionController() 
		# ||=======================||
		socket.setdefaulttimeout(1)
		self.listener = socket.socket()

	def jsonify(self):
		return {
			"Type": self.type,
			"Host": self.host,
			"Port": self.port
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

		return {	
			"Status": True,
			"_Class": self.type,
			"Message": "Server Created @: " + str(self.host) + ", Port: " + str(self.port),
			"Time": (time() - WATCH)
		}

	def listen(self):
		WATCH = time()
		self.listener.listen(500)
		self.active = True
		listenProtocalThread = Thread(target = self.beginListenProtocal)
		listenProtocalThread.setDaemon(True)
		listenProtocalThread.start()
		return {	
			"Status": True,
			"_Class": self.type,
			"Message": "Server Listening @: " + str(self.host) + ", Port: " + str(self.port),
			"Time": (time() - WATCH)
		}

	def beginListenProtocal(self):
		WATCH = time()
		while self.active:
			if (self.connectionStatus == False):
				try:
					print("Listening")
					conn, addr = self.listener.accept()
					print("Connection Created:","Address:",addr[0],"Port:",addr[1])
					self.connectionStatus = True
					self.connectionController.connectionCycle(conn, addr)
					self.connectionStatus = False
					conn.close()
				except socket.timeout as e:
					continue
				except Exception as e:
					print(e)
					return {	
						"Status": True,
						"_Class": "NetworkProtocalController",
						"Message": "Failure In Accepting Connection(s)",
						"Time": (time() - WATCH)
					}

	def closeServer(self):
		WATCH = time()
		self.active = False
		sleep(0.1)
		self.listener.close()
		return {	
			"Status": True,
			"_Class": self.type,
			"Message": "Server Closed",
			"Time": (time() - WATCH)
		}
