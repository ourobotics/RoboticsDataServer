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
from EngineData import EngineData
# Premades
from time import strftime, localtime
from flask import Flask, request, Response
import flask
from flask_restful import Resource, Api
from json import dumps, loads
from flask_jsonpify import jsonify
from flask_login import login_required
# ||=======================||
# Global Variables

# ||=======================||
# Notes

# ||=======================||
# ||===============================================================||

class EnergyControllerAPI(Resource):
	@login_required
	def get(self):
		dumpTag = request.args.get('dump')
		Data = str(EngineData.EnergyController.getLiveData())
		if (Data == "None"):
			resp = "No Information Found"
			resp = Response(resp)
			resp.headers['Access-Control-Allow-Origin'] = '*'
			return resp
		Data = Data.replace("'", '"')
		Data = Data.replace("True", "true")
		Data = Data.replace("False", "false")
		
		# ||=======================||
		resp = Response(Data)
		resp.headers['Access-Control-Allow-Origin'] = '*'
		if (dumpTag == "True"):
			jsonObj = loads(Data)
			resp = dumps(jsonObj, indent = 4)
			resp = resp.replace("\n", "<br>").replace("\\","")
			resp = Response(resp)
			resp.headers['Access-Control-Allow-Origin'] = '*'
		return resp

class ThermoControllerAPI(Resource):
	# @login_required
	def get(self):
		dumpTag = request.args.get('dump')
		Data = str(EngineData.ThermoController.getLiveData())
		Data = Data.replace("'", '"')
		Data = Data.replace("True", "true")
		Data = Data.replace("False", "false")
		
		# ||=======================||
		resp = Response(Data)
		resp.headers['Access-Control-Allow-Origin'] = '*'
		if (dumpTag == "True"):
			jsonObj = loads(Data)
			resp = dumps(jsonObj, indent = 4)
			resp = resp.replace("\n", "<br>").replace("\\","")
			resp = Response(resp)
			resp.headers['Access-Control-Allow-Origin'] = '*'
		return resp

class GpsControllerAPI(Resource):
	@login_required
	def get(self):
		dumpTag = request.args.get('dump')
		Data = str(EngineData.GpsController.getLiveData())
		Data = Data.replace("'", '"')
		Data = Data.replace("True", "true")
		Data = Data.replace("False", "false")
		
		# ||=======================||
		resp = Response(Data)
		resp.headers['Access-Control-Allow-Origin'] = '*'
		if (dumpTag == "True"):
			jsonObj = loads(Data)
			resp = dumps(jsonObj, indent = 4)
			resp = resp.replace("\n", "<br>").replace("\\","")
			resp = Response(resp)
			resp.headers['Access-Control-Allow-Origin'] = '*'
		return resp

class NetworkServerAPI(Resource):
	# @login_required
	def get(self):
		dumpTag = request.args.get('dump')
		Data = str(DeviceData.NetworkServer.getLiveData())
		Data = Data.replace("'", '"')
		Data = Data.replace("True", "true")
		Data = Data.replace("False", "false")
		
		# ||=======================||
		resp = Response(Data)
		resp.headers['Access-Control-Allow-Origin'] = '*'
		if (dumpTag == "True"):
			jsonObj = loads(Data)
			resp = dumps(jsonObj, indent = 4)
			resp = resp.replace("\n", "<br>").replace("\\","")
			resp = Response(resp)
			resp.headers['Access-Control-Allow-Origin'] = '*'
		return resp

class NetworkServerInternalLogAPI(Resource):
	@login_required
	def get(self):
		dumpTag = request.args.get('dump')
		index = request.args.get('index')
		rawData = DeviceData.NetworkServer.getInternalLog(index)
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
		if (dumpTag == "True"):
			jsonObj = loads(obj)
			resp = dumps(jsonObj, indent = 4)
			resp = resp.replace("\n", "<br>").replace("\\","")
			resp = Response(resp)
			resp.headers['Access-Control-Allow-Origin'] = '*'
		return resp

class ConnectionControllerAPI(Resource):
	@login_required
	def get(self):
		dumpTag = request.args.get('dump')
		Data = str(DeviceData.ConnectionController.getLiveData())
		Data = Data.replace("'", '"')
		Data = Data.replace("True", "true")
		Data = Data.replace("False", "false")

		# ||=======================||
		resp = Response(Data)
		resp.headers['Access-Control-Allow-Origin'] = '*'
		if (dumpTag == "True"):
			jsonObj = loads(Data)
			resp = dumps(jsonObj, indent = 4)
			resp = resp.replace("\n", "<br>").replace("\\","")
			resp = Response(resp)
			resp.headers['Access-Control-Allow-Origin'] = '*'
		return resp

class ConnectionControllerInteractionLogAPI(Resource):
	@login_required
	def get(self):
		dumpTag = request.args.get('dump')
		index = request.args.get('index')
		rawData = DeviceData.ConnectionController.getInteractionLog(index)
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
		if (dumpTag == "True"):
			jsonObj = loads(obj)
			resp = dumps(jsonObj, indent = 4)
			resp = resp.replace("\n", "<br>").replace("\\","")
			resp = Response(resp)
			resp.headers['Access-Control-Allow-Origin'] = '*'
		return resp

class ConnectionControllerInternalLogAPI(Resource):
	@login_required
	def get(self):
		dumpTag = request.args.get('dump')
		index = request.args.get('index')
		rawData = DeviceData.ConnectionController.getInternalLog(index)
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
		if (dumpTag == "True"):
			jsonObj = loads(obj)
			resp = dumps(jsonObj, indent = 4)
			resp = resp.replace("\n", "<br>").replace("\\","")
			resp = Response(resp)
			resp.headers['Access-Control-Allow-Origin'] = '*'
		return resp

class ApiService(object):
	def __init__(self, app):
		self.type = "ApiService"
		self.active = True
		app.debug = False
		self.log = False
		self.api = Api(app)
		# Energy Controller Api
		self.api.add_resource(EnergyControllerAPI, '/energycontroller/api')
		# Thermo Controller Api
		self.api.add_resource(ThermoControllerAPI, '/thermocontroller/api')
		# Gps Controller Api
		self.api.add_resource(GpsControllerAPI, '/gpscontroller/api')
		# Network Server Api
		self.api.add_resource(NetworkServerAPI, '/networkserver/api')
		# Network Server Internal Log Api
		self.api.add_resource(NetworkServerInternalLogAPI, '/nsl/api')
		# Connection Controller Api
		self.api.add_resource(ConnectionControllerAPI, '/connectioncontroller/api')
		# Connection Controller Interaction Log Api
		self.api.add_resource(ConnectionControllerInteractionLogAPI, '/ccil/api')
		# Connection Controller Internal Log Api
		self.api.add_resource(ConnectionControllerInternalLogAPI, '/ccl/api')

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
				"Port": self.port,
				"Log": self.log
			}
		}

# |===============================================================|