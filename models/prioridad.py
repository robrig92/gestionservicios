from mongoengine import *


connect('gestionservicios')


class Prioridad(Document):
	"""
		Sprint: 1

		Modelo  que representa el 
	catálogo  de prioridad en el 
	sistema.

		@author Paulo_Angeles.
	"""
	_id					= ObjectIdField()
	enabled 			= BooleanField()
	hashId 				= StringField()
	nombre		 		= StringField()