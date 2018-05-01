from mongoengine import *


connect('gestionservicios')


class Servicio(Document):
	"""
		Sprint: 1

			Modelo  que representa un Servicio
		en el sistema.

		@author Paulo_Angeles.
	"""
	_id					= ObjectIdField()
	enabled	 			= BooleanField()
	createdAt 			= DateTimeField()
	updatedAt 			= DateTimeField()
	hashId 				= StringField()
	usuarioCreador 		= ObjectIdField()
	tipo 				= StringField()
	descripcion 		= StringField()
	precio				= DecimalField()
	observaciones		= StringField()
	tiempoPromedio		= StringField()
