from flask import Flask
from mongoengine import *
from .models.cliente import *


app = Flask(__name__)


@app.route('/')
def hello_world():
	clientes = ''
	for cliente in Cliente.objects.all():
		clientes += cliente.nombreContacto
	return clientes
