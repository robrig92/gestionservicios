from flask import Flask
from mongoengine import *
from .models.cliente import *
from .controllers.cliente_controller import ClienteController
from .controllers.usuario_controller import UsuarioController

app = Flask(__name__)


@app.route('/api/clientes')
def clientes_index():
	clienteController = ClienteController()
	return clienteController.index()


@app.route('/api/usuarios')
def usuarios_index():
	usuarioController = UsuarioController()
	return usuarioController.index()
