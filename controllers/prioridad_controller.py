from flask import Blueprint, request
from ..models.prioridad import Prioridad
from ..utils.StringUtils import StringUtils
import datetime
import time
from bson import ObjectId


prioridad = Blueprint('prioridad', __name__)
"""	    

	Controller encargado de las operaciones relacionadas
con prioridades (catálogo).

    @author Paulo_Angeles.
"""
@prioridad.route('', methods=['GET'])
def list():
	"""
		Sprint: 1.

			Método encargado de listar todos
		las prioridades(catálogo) existentes
		en el sistema

		@author Paulo_Angeles.
	"""
	print("REQUEST GET. List prioridades.")
	prioridades = Prioridad.objects()
	return prioridades.to_json()

@prioridad.route('/<hashId>', methods=['GET'])
def get( hashId ):
	"""
		Sprint: 1.

			Método encargado de obtener una
		prioridad(catálogo) determinada
		mediante su campo hash_id.

		@author Paulo_Angeles.
	"""
	print("REQUEST GET. Get prioridad hashId = " + hashId )
	prioridad = Prioridad.objects.get(hashId=hashId)
	return prioridad.to_json()

@prioridad.route('', methods=['POST'])
def save( ):

	"""
		Sprint: 1.

			Método encargado de persistir una
		prioridad(catálogo) en el sitema.

		@author Paulo_Angeles.
	"""
	print("REQUEST POST. Create prioridad.")
	prioridad 					= Prioridad()
	prioridad.enabled 			= True
	prioridad.hashId 			= StringUtils.randomHash();
	prioridad.nombre	 		= request.form.get( 'nombre'			, 'Nombre por defecto' )
	prioridad.save()
	return 'success create'

@prioridad.route('/<hashId>', methods=['PATCH'])
def update( hashId ):
	"""
		Sprint: 1.

			Método encargado de actualizar una
		prioridad (catálogo) en el sitema.

		@author Paulo_Angeles.
	"""
	print("REQUEST PATCH. Update prioridad hashId = " + hashId )
	prioridad 						= Prioridad.objects.get(hashId=hashId)
	prioridad.nombre	 			= request.form.get( 'nombre'			, 'Nombre por defecto ' + str( time.time() ) )
	prioridad.save()
	return 'success update'
