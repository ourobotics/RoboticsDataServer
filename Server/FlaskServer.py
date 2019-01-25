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
from flask import Flask, request, Response, redirect, url_for
import flask
from flask_restful import Resource
from json import dumps, loads
from flask_jsonpify import jsonify
from flask_login import LoginManager, login_user, login_required, user_logged_in, current_user
# import flask_login
# ||=======================||
# Global Variables
# ||=======================||
# Notes
# ||=======================||
# ||===============================================================||

UserList = {}

class User(object):
	def __init__(self, id, username, active=True):
		self.username = username
		self.id = id
		self.active = active
		#self.active = active
	def is_authenticated(self):
		return True

	def is_active(self):
		return self.active

	def is_anonymous(self):
		return False

	def get_id(self):
		return self.id

app = Flask(__name__, template_folder='../templates', static_folder='../Static')
app.secret_key = b'_5#y2L"F4Qa8z\n\xec]/'

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
	# print(user_id)
	try:
		return UserList[user_id]
	except:
		return None

@app.route("/energycontroller")
@login_required
def energycontroller():
	return flask.render_template("json.html", variable="energycontroller")

@app.route("/thermocontroller")
@login_required
def thermocontroller():
	return flask.render_template("json.html", variable="thermocontroller")

@app.route("/gpscontroller")
@login_required
def gpscontroller():
	return flask.render_template("json.html", variable="gpscontroller")

@app.route("/networkserver")
@login_required
def networkserver():
	return flask.render_template("json.html", variable="networkserver")

@app.route("/nsl")
@login_required
def nsl():
	return flask.render_template("json.html", variable="nsl")

@app.route("/connectioncontroller")
@login_required
def connectioncontroller():
	return flask.render_template("json.html", variable="connectioncontroller")

@app.route("/ccil")
@login_required
def ccil():
	return flask.render_template("json.html", variable="ccil")

@app.route("/ccl")
@login_required
def ccl():
	return flask.render_template("json.html", variable="ccl")

@app.route("/test")
@login_required
def test():
	return flask.render_template("test.html")

@app.route("/dashboard")
@login_required
def dashboard():
	return flask.render_template("dashboard.html")

@app.route("/")
@app.route("/index")
@login_required
def index():
	return flask.render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
	if (current_user.is_authenticated):
		return redirect(url_for('index'))

	if (request.method == "POST"):
		if ((request.form['username'] != 'admin') or (request.form['password'] != 'admin')):
			username = request.form['username']
			password = request.form['password']
			# print(username, password)
			error = 'Invalid Credentials. Please try again.'
		else:
			username = request.form['username']
			password = request.form['password']
			# print(username, password)
			user = User(hash(username), username)
			UserList[hash(username)] = user
			login_user(user)

			flask.flash('Logged in successfully.')

			# print("Success")
			return redirect(url_for('index'))
	return flask.render_template("login.html")

class FlaskServer(object):
	def __init__(self, useApiService = False):
		self.type = "FlaskServer"
		self.active = True
		app.debug = True
		self.address = "0.0.0.0"
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

		login_manager.init_app(app)
		login_manager.login_view = 'login'

		app.run(host=self.address,port=self.port, use_evalex=self.log)
		
# |===============================================================|