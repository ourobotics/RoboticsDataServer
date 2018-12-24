# ||==============================================================||
# ||
# ||  Program/File:     FlaskServer
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
from ApiService import ApiService
# Controllers
# Tools
# Test
# Data
from DeviceData import DeviceData
# Premades
from flask import Flask, request, Response
import flask
from flask_restful import Resource
from json import dumps, loads
from flask_jsonpify import jsonify
# ||=======================||
# Global Variables
# ||=======================||
# Notes
# ||=======================||
# ||===============================================================||

app = Flask(__name__, template_folder='../templates')

@app.route("/networkserver")
def networkserver():
	# # firstName = request.args.get('first_name')
	Data = str(DeviceData.getLiveDeviceData()["NetworkServer"])
	Data = Data.replace("'", '"')
	Data = Data.replace("True", "true")
	Data = Data.replace("False", "false")
	
	jsonObj = loads(Data)
	# ||=======================||
	resp = Response(jsonObj)
	resp.headers['Access-Control-Allow-Origin'] = '*'
	resp = dumps(jsonObj, indent = 4)
	return flask.render_template("json.html", name=resp)

@app.route("/connectioncontroller")
def connectioncontroller():
	Data = str(DeviceData.getLiveDeviceData()["ConnectionController"])
	Data = Data.replace("'", '"')
	Data = Data.replace("True", "true")
	Data = Data.replace("False", "false")

	jsonObj = loads(Data)
	# ||=======================||
	resp = Response(jsonObj)
	resp.headers['Access-Control-Allow-Origin'] = '*'
	resp = dumps(jsonObj, indent = 4)
	return flask.render_template("json.html", name=resp)

@app.route("/ccil")
def ccil():
	index = request.args.get('index')
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

	jsonObj = loads(obj)
	# ||=======================||
	resp = Response(jsonObj)
	resp.headers['Access-Control-Allow-Origin'] = '*'
	resp = dumps(jsonObj, indent = 4)
	return flask.render_template("json.html", name=resp)

class FlaskServer(object):
	def __init__(self, useApiService = False):
		self.type = "FlaskServer"
		self.active = True
		app.debug = False
		self.address = "192.168.0.6"
		self.port = '5002'
		self.log = False
		self.useApiService = useApiService

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

	def FlaskServerThread(self):
		if (self.useApiService == True):
			apiService = ApiService(app)


		app.run(host=self.address,port=self.port, use_evalex=self.log)
		
# |===============================================================|