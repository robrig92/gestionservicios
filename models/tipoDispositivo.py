from mongoengine import *


connect('gestionservicios')


class TipoDispositivo(Document):
	"""
		Sprint: 1

		Modelo  que representa tipos 
	de dispositvos en el sistema.

		@author Paulo_Angeles.
	"""
	_id					= ObjectIdField()
	enabled	 			= BooleanField()
	createdAt 			= DateTimeField()
	updatedAt 			= DateTimeField()
	hashId 				= StringField()
	usuarioCreador 		= ObjectIdField()
	tipo 				= StringField()
	meta 				=  { 'collection' :  'tipoDispositivo' }