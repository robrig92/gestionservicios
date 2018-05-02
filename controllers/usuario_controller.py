import datetime
from bson import ObjectId
from ..models.usuario import Usuario
from flask import Blueprint, request
from ..utils.StringUtils import StringUtils

usuario = Blueprint('usuario', __name__)
"""
	Contusuarioador de modelo Usuario.

	@author Roberto_Padilla
"""
@usuario.route('/', methods=['GET'])
def index():
	"""
		Sprint 1:

		Método index recupera todos los usuarios
		del almacenamiento de datos.

		@author Roberto_Padilla
	"""
	usuarios = Usuario.objects()
	return usuarios.to_json()

@usuario.route('/<hashId>', methods=['GET'])
def show(hashId):
	"""
		Sprint 1:

		Este método recupera un documento usuario por medio
		de su hashId.

		@author Roberto_Padilla
	"""
	usuario = Usuario.objects(hashId=hashId)
	return usuario.to_json()

@usuario.route('/', methods=['POST'])
def store():
	"""
		Sprint 1:

		Este método almacena un documento en la
		base de datos.

		@author Roberto_Padilla
	"""
	if request.form.get('enabled') == '1':
		enabled = True
	else:
		enabled = False
	usuario = Usuario()
	usuario.enabled = enabled
	usuario.createdAt = datetime.datetime.utcnow()
	usuario.updatedAt = datetime.datetime.utcnow()
	usuario.hashId = StringUtils.randomHash()
	usuario.usuarioCreador = ObjectId(request.form['usuarioCreador'])
	usuario.nombre = request.form['nombre']
	usuario.email = request.form['email']
	usuario.telefono = request.form['telefono']
	usuario.imagenPerfil = ObjectId(request.form['imagenPerfil'])
	usuario.nickname = request.form['nickname']
	usuario.rol_id = ObjectId(request.form['rol_id'])
	usuario.save()
	return 'success'

@usuario.route('/<hashId>', methods=['PATCH'])
def patch(hashId):
	"""
		Sprint 1:

		Este método actualiza la información de un documento
		en la base de datos identificándolo por medio de
		su hashId.

		@author Roberto_Padilla
	"""
	usuario = Usuario.objects.get(hashId=hashId)
	if request.form.get('enabled') == '1':
		enabled = True
	else:
		enabled =  False
	usuario.enabled = enabled
	usuario.updatedAt = datetime.datetime.utcnow()
	usuario.nombre = request.form['nombre']
	usuario.email = request.form['email']
	usuario.telefono = request.form['telefono']
	usuario.imagenPerfil = ObjectId(request.form['imagenPerfil'])
	usuario.nickname = request.form['nickname']
	usuario.rol_id = ObjectId(request.form['rol_id'])
	usuario.save()
	return 'success'
