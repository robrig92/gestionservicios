from flask import Blueprint, request
from ..models.servicio import Servicio
from ..utils.StringUtils import StringUtils
import datetime
import time
from bson import ObjectId


servicio = Blueprint('servicio', __name__)
"""
    Controller encargado de las operaciones relacionadas
con servicios

    @author Paulo_Angeles.
"""
@servicio.route('', methods=['GET'])
def list():
	"""
		Sprint: 1.

			Método encargado de listar todos
		los servicios existentes
		en el sistema

		@author Paulo_Angeles.
	"""
	print("REQUEST GET. List servicios.")
	servicios = Servicio.objects()
	return servicios.to_json()

@servicio.route('/<hashId>', methods=['GET'])
def get( hashId ):
	"""
		Sprint: 1.

			Método encargado de obtener un
		servicio determinado
		mediante su campo hash_id.

		@author Paulo_Angeles.
	"""
	print("REQUEST GET. Get servicio hashId = " + hashId )
	servicio = Servicio.objects.get(hashId=hashId)
	return servicio.to_json()

@servicio.route('', methods=['POST'])
def save( ):

	"""
		Sprint: 1.

			Método encargado de persistir un
		servicio en el sitema.

		@author Paulo_Angeles.
	"""
	print("REQUEST POST. Create Servicio.")
	servicio 					= Servicio()
	servicio.enabled 			= True
	servicio.createdAt 			= datetime.datetime.utcnow()
	servicio.updatedAt 			= datetime.datetime.utcnow()
	servicio.hashId 			= StringUtils.randomHash();
	servicio.usuarioCreador 	= ObjectId(request.form.get('usuarioCreador', '5adf9abc30c9451b476ee260' ) )
	servicio.descripcion		= request.form.get('descripcion', 'Descripcion por defecto.');
	servicio.precio				= request.form.get('precio', 25500.55);
	servicio.observaciones		= request.form.get('observaciones', 'Observaciones por defecto.');
	servicio.tiempoPromedio		= request.form.get('tiempo_promedio', 'Tiempo Promedio por defecto.');

	servicio.save()
	return 'success create'

@servicio.route('/<hashId>', methods=['PATCH'])
def update( hashId ):
	"""
		Sprint: 1.

			Método encargado de actualizar un
		servicio en el sitema.

		@author Paulo_Angeles.
	"""
	print("REQUEST PATCH. Update servicio hashId = " + hashId )
	servicio 					= Servicio.objects.get(hashId=hashId)
	servicio.updatedAt 			= datetime.datetime.utcnow()
	servicio.descripcion		= request.form.get('descripcion', 'Descripcion por defecto.' + str( time.time() ) );
	servicio.precio				= request.form.get('precio', 15500.55);
	servicio.observaciones		= request.form.get('observaciones', 'Observaciones por defecto.' + str( time.time() ) );
	servicio.tiempoPromedio		= request.form.get('tiempo_promedio', '15h' );
	servicio.save()
	return 'success update'
