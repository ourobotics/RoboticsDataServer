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
# ||=======================||
# Routes
# Controllers

# Tools

# Test

# Premades
from time import time
from _thread import start_new_thread
import traceback
import socket
# ||=======================||
# Global Variables

# ||=======================||
# Notes

# ||=======================||
# |============================================================================|

class ConnectionController(object):
	def __init__(self):
		self.active = True


	def connectionCycle(self, conn, addr):
		WATCH = time()
		while self.active:
			try:
				# print("reqw")
				dataRecv = conn.recv(1024).decode()
			except Exception as e:
				return {	
					"Status": False,
					"_Class": "NetworkProtocalController",
					"Message": "Successfully Closing Thread -> readSocketCycle",
					"Time": (time() - WATCH)
				}

			CODE = dataRecv[:6]

			# ||=======================||
			# Return Connection Success
			if CODE == "#00000":
				conn.send(("Success").encode())
				print("Success")
				# self.LoggingTool.Log("Sending Connecting Created!")

			# ||=======================||
			# Test Server Connection
			elif CODE == "#00001":
				conn.send(("Success").encode())
				# self.LoggingTool.Log("Sending Connecting Success!")

			# ||=======================||
			# Write Data To DeviceData
			elif CODE == "#00002":
				conn.send(("Success").encode())
				tmpData = dataRecv[7:]
				DeviceData.setDeviceData(tmpData)
				print("Device Data:", tmpData)

			# ||=======================||
			# Retry Arduino Connection
			# elif CODE == "#00003":
				# start_new_thread(microControllerController.microControllerConnection,())

			# ||=======================||
			# Close Client Connection
			elif CODE == "#99999":
				conn.send(("Success").encode())
				return

			dataRecv = ""

		return