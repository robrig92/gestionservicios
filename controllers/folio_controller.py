import datetime
from bson import ObjectId
from ..models.folio import Folio
from flask import Blueprint, request
from ..utils.StringUtils import StringUtils

folio = Blueprint('folio', __name__)
"""
	Contfolioador de modelo Folio.

	@author Roberto_Padilla
"""
@folio.route('/', methods=['GET'])
def index():
	"""
		Sprint 1:

		Método index recupera todos los folios
		del almacenamiento de datos.

		@author Roberto_Padilla
	"""
	folios = Folio.objects()
	return folios.to_json()

@folio.route('/<hashId>', methods=['GET'])
def show(hashId):
	"""
		Sprint 1:

		Este método recupera un documento folio por medio
		de su hashId.

		@author Roberto_Padilla
	"""
	folio = Folio.objects(hashId=hashId)
	return folio.to_json()

@folio.route('/', methods=['POST'])
def store():
	"""
		Sprint 1:

		Este método almacena un documento en la
		base de datos.

		@author Roberto_Padilla
	"""
	if request.form['enabled'] == '1':
		enabled = True
	else:
		enabled = False
	fechaAbre = datetime.datetime.strptime(request.form['fechaAbre'], '%d/%m/%Y %H:%M:%S')
	fechaCierre = datetime.datetime.strptime(request.form['fechaCierre'], '%d/%m/%Y %H:%M:%S')
	folio = Folio()
	folio.enabled = enabled
	folio.createdAt = datetime.datetime.utcnow()
	folio.updatedAt = datetime.datetime.utcnow()
	folio.hashId = StringUtils.randomHash()
	folio.usuarioCreador = ObjectId(request.form['usuarioCreador'])
	folio.cliente_id = ObjectId(request.form['cliente_id'])
	folio.servicio_id = ObjectId(request.form['servicio_id'])
	folio.asignadoA = ObjectId(request.form['asignadoA'])
	folio.prioridad_id = ObjectId(request.form['prioridad_id'])
	folio.cotizacion = request.form['cotizacion']
	folio.total = request.form['total']
	folio.fechaAbre = fechaAbre
	folio.fechaCierre = fechaCierre
	folio.estatus_id = request.form['estatus_id']
	folio.numeroSerie = request.form['numeroSerie']
	folio.tipoDispositivo_id = request.form['tipoDispositivo_id']
	folio.marca_id = request.form['marca_id']
	folio.observaciones = request.form['observaciones']
	folio.save()
	return 'success'

@folio.route('/<hashId>', methods=['PATCH'])
def patch(hashId):
	"""
		Sprint 1:

		Este método actualiza la información de un documento
		en la base de datos identificándolo por medio de
		su hashId.

		@author Roberto_Padilla
	"""
	folio = Folio.objects.get(hashId=hashId)
	if request.form['enabled'] == '1':
		enabled = True
	else:
		enabled =  False
	fechaAbre = datetime.datetime.strptime(request.form['fechaAbre'], '%d/%m/%Y %H:%M:%S')
	fechaCierre = datetime.datetime.strptime(request.form['fechaCierre'], '%d/%m/%Y %H:%M:%S')
	folio.enabled = enabled
	folio.updatedAt = datetime.datetime.utcnow()
	folio.cliente_id = ObjectId(request.form['cliente_id'])
	folio.servicio_id = ObjectId(request.form['servicio_id'])
	folio.asignadoA = ObjectId(request.form['asignadoA'])
	folio.prioridad_id = ObjectId(request.form['prioridad_id'])
	folio.cotizacion = request.form['cotizacion']
	folio.total = request.form['total']
	folio.fechaAbre = fechaAbre
	folio.fechaCierre = fechaCierre
	folio.estatus_id = request.form['estatus_id']
	folio.numeroSerie = request.form['numeroSerie']
	folio.tipoDispositivo_id = request.form['tipoDispositivo_id']
	folio.marca_id = request.form['marca_id']
	folio.observaciones = request.form['observaciones']
	folio.save()
	return 'success'
