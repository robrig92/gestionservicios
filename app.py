from flask import Flask
from mongoengine import *
from models.cliente import Cliente


app = Flask(__name__)


@app.route('/')
def hello_world():
	clientes = ''
	for cliente in Cliente.objects:
		clientes += cliente.nombreContacto
	return clientes
