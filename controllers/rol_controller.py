import datetime
from bson import ObjectId
from ..models.rol import Rol
from flask import Blueprint, request
from ..utils.StringUtils import StringUtils

rol = Blueprint('rol', __name__)
"""
	Controlador de modelo Rol.

	@author Roberto_Padilla
"""
@rol.route('/', methods=['GET'])
def index():
	"""
		Sprint 1:

		Método index recupera todos los roles
		del almacenamiento de datos.

		@author Roberto_Padilla
	"""
	roles = Rol.objects()
	return roles.to_json()

@rol.route('/<hashId>', methods=['GET'])
def show(hashId):
	"""
		Sprint 1:

		Este método recupera un documento rol por medio
		de su hashId.

		@author Roberto_Padilla
	"""
	roles = Rol.objects(hashId=hashId)
	return roles.to_json()

@rol.route('/', methods=['POST'])
def store(request):
	"""
		Sprint 1:

		Este método almacena un documento en la
		base de datos.

		@author Roberto_Padilla
	"""
	if request.form['enabled'] == 1:
		enabled = True
	else:
		enabled = False
	rol = Rol()
	rol.enabled = enabled
	rol.createdAt = datetime.datetime.utcnow()
	rol.updatedAt = datetime.datetime.utcnow()
	rol.hashId = StringUtils.randomHash()
	rol.usuarioCreador = ObjectId(request.form['usuarioCreador'])
	rol.nombre = request.form['nombre']
	rol.save()
	return 'success'

@rol.route('/<hashId>', methods=['PATCH'])
def patch(hashId, request):
	"""
		Sprint 1:

		Este método actualiza la información de un documento
		en la base de datos identificándolo por medio de
		su hashId.

		@author Roberto_Padilla
	"""
	rol = Rol.objects.get(hashId=hashId)
	if request.form.get('nombre', 1) == 1:
		enabled = True
	else:
		enabled =  False
	rol.enabled = enabled
	rol.updatedAt = datetime.datetime.utcnow()
	rol.nombre = request.form.get('nombre', 'VALOR POR DEFECTO')
	rol.save()
	return 'success'
