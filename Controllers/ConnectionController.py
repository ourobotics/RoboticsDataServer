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
# Premades
from time import time, strftime, localtime
from _thread import start_new_thread
import traceback
import socket
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
				"Address": str(self.address[0]) + ', ' + str(self.address[1])
			}
		}

	def setConnection(self, conn, addr):
		self.connection = conn
		self.address = addr

	def createInteractionLog(self, dataRecv):
		return self.jsonify(
			str(dataRecv),
			str(strftime("%Y-%m-%d %H:%M:%S", localtime())),
			"createInteractionLog"
		)

	def connectionCycle(self):
		WATCH = time()
		
		if (self.connection == None or self.address == None):
			self.active = False
			return self.jsonify(
				"Invalid address or connection",
				time()-WATCH, 
				"connectionCycle"
			)
		
		while self.active:
			dataRecv = None
			try:
				dataRecv = self.connection.recv(1024).decode()
				print(dataRecv)
			except socket.timeout as e:
					continue
			except Exception as e:
				print(e)
				self.active = False
				return self.jsonify(
					"Successfully Closing Thread -> readSocketCycle",
					time()-WATCH, 
					"connectionCycle"
				)

			if (dataRecv != None):

				CODE = dataRecv[:6]

				# ||=======================||
				# Return Connection Success
				if (CODE == "#00000"):
					self.connection.send(("Success").encode())
					DeviceData.appendInteractionLog(self.createInteractionLog(dataRecv))
					print("Success")


				# ||=======================||
				# Test Server Connection
				elif (CODE == "#00001"):
					self.connection.send(("Success").encode())
					DeviceData.appendInteractionLog(self.createInteractionLog(dataRecv))

				# ||=======================||
				# Write Data To DeviceData
				elif (CODE == "#00002"):
					self.connection.send(("Success").encode())
					tmpData = dataRecv[7:]
					DeviceData.appendInteractionLog(self.createInteractionLog(dataRecv))
					print("Device Data:", tmpData)

				# ||=======================||
				# Retry Arduino Connection
				# elif CODE == "#00003":
					# start_new_thread(microControllerController.microControllerConnection,())

				# ||=======================||
				# Close Client Connection
				elif (CODE == "#99999"):
					self.connection.send(("Success").encode())
					return

				dataRecv = None

		return

# |===============================================================|