from flask import Flask
from mongoengine import *
from .models.cliente import *
app = Flask(__name__)
from .controllers.cliente_controller import ClienteController

@app.route('/api/clientes')
def hello_world():
	clienteController = ClienteController()
	return clienteController.index().to_json()
