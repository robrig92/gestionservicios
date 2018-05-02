import datetime
from bson import ObjectId
from ..models.marca import Marca
from flask import Blueprint, request
from ..utils.StringUtils import StringUtils

marca = Blueprint('marca', __name__)
"""
	Controlador de modelo Marca.

	@author Roberto_Padilla
"""
@marca.route('/', methods=['GET'])
def index():
	"""
		Sprint 1:

		Método index recupera todos los documentos marca
		del almacenamiento de datos.

		@author Roberto_Padilla
	"""
	marcas = Marca.objects()
	return marcas.to_json()

@marca.route('/<id>', methods=['GET'])
def show(id):
	"""
		Sprint 1:

		Este método recupera un documento marca por medio
		de su id.

		@author Roberto_Padilla
	"""
	marca = Marca.objects(id=id)
	return marca.to_json()

@marca.route('/', methods=['POST'])
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
	marca = Marca()
	marca.enabled = enabled
	marca.createdAt = datetime.datetime.utcnow()
	marca.updatedAt = datetime.datetime.utcnow()
	marca.usuarioCreador = ObjectId(request.form['usuarioCreador'])
	marca.marca = request.form['marca']
	marca.save()
	return 'success'

@marca.route('/<id>', methods=['PATCH'])
def patch(id):
	"""
		Sprint 1:

		Este método actualiza la información de un documento
		en la base de datos identificándolo por medio de
		su id.

		@author Roberto_Padilla
	"""
	marca = Marca.objects.get(id=id)
	if request.form.get('enabled') == '1':
		enabled = True
	else:
		enabled =  False
	marca.enabled = enabled
	marca.updatedAt = datetime.datetime.utcnow()
	marca.marca = request.form.get('marca', 'VALOR POR DEFECTO')
	marca.save()
	return 'success'
