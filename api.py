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


UserDict = {}

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(32), unique=True)
	password_hash = db.Column(db.String(64))
	nickname = db.Column(db.String(32), unique=True)
	money = db.Column(db.Integer)

	def hash_password(self, password):
		self.password_hash = pwd_context.encrypt(password)
	
	def verify_password(self, password):
		return pwd_context.verify(password, self.password_hash)	


@app.route('/time_store/api/direction',methods=['POST'])
def direction():
	direction = request.json.get("direction")
	print direction
	return "Post Direction Success"

@app.route('/time_store/api/register',methods=['POST'])
def register():
	username = request.json.get('username')
	password = request.json.get('password')
	if username is None or password is None:
		return "Wrong Parameter"
	if User.query.filter_by(username=username).first() is not None:
		return "User Existed"
	user = User(username=username)
	user.hash_password(password)
	db.session.add(user)
	db.session.commit()
	return "Success"

@app.route('/time_store/api/login', methods=['POST'])
def login():
	username = request.json.get('username')
	password = request.json.get('password')
	user = User.query.filter_by(username=username).first()
	if not user:
		return "Wrong User"
	if not user.verify_password(password):
		return "Wrong Password"
	return "Login Successfully"

@app.route('/time_store/api')
def test():
	return "Hello"

	

if __name__ == '__main__':
	if not os.path.exists('db.sqlite'):
		db.create_all()
	app.run(host="0.0.0.0",port=5000,debug=True)

