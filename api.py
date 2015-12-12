# -*-coding: utf-8 -*-
import os
from flask import Flask, abort, request, jsonify, g, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import (TimedJSONWebSignatureSerializer 
						  as Serializer, BadSignature, SignatureExpired)
from werkzeug.exceptions import HTTPException

# Initialization
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SECRET_KEY'] = "the api works for the time store app"
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

# Extensions
db = SQLAlchemy(app)
auth =  HTTPBasicAuth()


User = {}



@app.route('/time_store/api/user',methods=['POST'])
def user_check():
	username = request.json.get('username')
	if username == "YinYuning":
		user1 = True
		return jsonify({"message":"Login Success!"})
	if username == "ShiPeng":
		user2 = True
		return jsonify({"message":"Login Success!"})
	return jsonify({"message":"Login Failed!"})

@app.route('/time_store/api/direction',methods=['POST'])
def direction():
	direction = request.json.get("direction")
	print direction
	return "Post Direction Success"

@app.route('/time_store/api/register',methods=['POST'])
def register():
	username = request.json.get('username')
	password = request.json.get('password')
	User[username] = password
	return "Success"

@app.route('/time_store/api/login', methods=['POST'])
def login():
	username = request.json.get('username')
	password = request.json.get('password')
	if username in User:
		if User[username] == password:
			return"Login Successfully"
		else:
			return "Wrong Password"
	else:
		return "Wrong Username"

@app.route('/time_store/api')
def test():
	return "Hello"

	

if __name__ == '__main__':
	app.run(host="0.0.0.0",port=5000,debug=True)

