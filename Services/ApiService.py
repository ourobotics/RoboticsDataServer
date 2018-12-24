# ||==============================================================||
# ||
# ||  Program/File:     ApiService.py
# ||
# ||  Description:				
# ||
# ||  Author:           Logan Wilkovich
# ||  Email:            LWilkovich@gmail.com
# ||  Creation Date:    24 December 2018 | Logan Wilkovich
# ||===============================================================||
# ||===============================================================||
# ||=======================||
# Routes
# Server
# Services
# Controllers
# Tools
# Test
# Data
from DeviceData import DeviceData
# Premades
from flask import Flask, request, Response
import flask
from flask_restful import Resource, Api
from json import dumps, loads
from flask_jsonpify import jsonify
# ||=======================||
# Global Variables

# ||=======================||
# Notes

# ||=======================||
# ||===============================================================||

class NetworkServerAPI(Resource):
	def get(self):
		Data = str(DeviceData.getLiveDeviceData()["NetworkServer"])
		Data = Data.replace("'", '"')
		Data = Data.replace("True", "true")
		Data = Data.replace("False", "false")
		
		# ||=======================||
		resp = Response(Data)
		resp.headers['Access-Control-Allow-Origin'] = '*'
		return resp

class ConnectionControllerAPI(Resource):
	def get(self):
		Data = str(DeviceData.getLiveDeviceData()["ConnectionController"])
		Data = Data.replace("'", '"')
		Data = Data.replace("True", "true")
		Data = Data.replace("False", "false")

		# ||=======================||
		resp = Response(Data)
		resp.headers['Access-Control-Allow-Origin'] = '*'
		return resp

class ConnectionControllerInteractionLogAPI(Resource):
	def get(self):
		index = request.args.get('index')
		print(index)
		rawData = DeviceData.getInteractionLog(index)
		Data = str(rawData)
		Data = Data.replace("'", '"')
		Data = Data.replace("True", "true")
		Data = Data.replace("False", "false")
		obj = '{'
		if (index == None):
			obj += '"Size":' + str(len(rawData)) + ','
		else:
			obj += '"Index":' + str(index) + ','
		obj += '"InteractionLogs":' + Data
		obj += '}'

		# ||=======================||
		resp = Response(obj)
		resp.headers['Access-Control-Allow-Origin'] = '*'
		return resp

class ApiService(object):
	def __init__(self, app):
		self.type = "ApiService"
		self.active = True
		app.debug = False
		self.log = False
		self.api = Api(app)
		# Network Server Api
		self.api.add_resource(NetworkServerAPI, '/networkserver/api')
		# Connection Controller Api
		self.api.add_resource(ConnectionControllerAPI, '/connectioncontroller/api')
		# Connection Controller Interaction Log Api
		self.api.add_resource(ConnectionControllerInteractionLogAPI, '/ccil/api')

	def jsonify(self, message = "Null", time = -1, function = "Null"):
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
				"Port": self.port,
				"Log": self.log
			}
		}

# |===============================================================|