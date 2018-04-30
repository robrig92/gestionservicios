from flask import Flask, request
from mongoengine import *
from .controllers.cliente_controller import ClienteController
from .controllers.usuario_controller import UsuarioController
from .controllers.rol_controller import RolController


app = Flask(__name__)


@app.route('/api/clientes')
def clientes_index():
	clienteController = ClienteController()
	return clienteController.index()

@app.route('/api/usuarios')
def usuarios_index():
	usuarioController = UsuarioController()
	return usuarioController.index()

@app.route('/api/roles')
def roles_index():
	rolController = RolController()
	return rolController.index()

@app.route('/api/roles/<hashId>')
def roles_show(hashId):
	rolController = RolController()
	return rolController.show(hashId)

@app.route('/api/roles/', methods=['POST'])
def roles_store():
	rolController = RolController()
	return rolController.store(request)

@app.route('/api/roles/<hashId>', methods={'PATCH'})
def roles_patch(hashId):
	RolController = RolController()
	return RolController.patch(hashId, request)
