from flask import Flask, request
from mongoengine import *
from .controllers.cliente_controller import cliente
from .controllers.tipoDispositivo_controller import tipoDispositivo
from .controllers.usuario_controller import UsuarioController
from .controllers.rol_controller import RolController
from .middleware.HTTPMethodOverrideMiddleware import HTTPMethodOverrideMiddleware

app = Flask(__name__)
app.wsgi_app = HTTPMethodOverrideMiddleware(app.wsgi_app)

# Routes para clientes
#@app.route('/api/clientes')
#def clientes_index():
#	clienteController = ClienteController()
#	return clienteController.index()

# Routes para usuarios
@app.route('/api/usuarios')
def usuarios_index():
	usuarioController = UsuarioController()
	return usuarioController.index()

# Routes para roles
@app.route('/api/roles')
def roles_index():
	rolController = RolController()
	return rolController.index()

@app.route('/api/roles/<hashId>', methods=['GET'])
def roles_show(hashId):
	print ('Request GET. Show rol with hashId = ' + hashId )
	rolController = RolController()
	return rolController.show(hashId)

@app.route('/api/roles/<hashId>', methods=['PATCH'])
def roles_update(hashId):
	print ('Request PATCH. Update rol with hashId = ' + hashId )
	rolController = RolController()
	return rolController.patch(hashId, request)

@app.route('/api/roles/', methods=['POST'])
def roles_store():
	rolController = RolController()
	return rolController.store(request)

app.register_blueprint( cliente 			, url_prefix='/api/cliente')
app.register_blueprint( tipoDispositivo 	, url_prefix='/api/tipodispositivo')