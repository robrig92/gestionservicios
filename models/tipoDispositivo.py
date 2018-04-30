from mongoengine import *


connect('gestionservicios')


class TipoDispositivo(Document):
	_id					= ObjectIdField()
	enabled	 			= BooleanField()
	createdAt 			= DateTimeField()
	updatedAt 			= DateTimeField()
	hashId 				= StringField()
	usuarioCreador 		= ObjectIdField()
	tipo 				= StringField()
	meta 				=  { 'collection' :  'tipoDispositivo' }