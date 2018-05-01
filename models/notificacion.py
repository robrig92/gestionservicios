from mongoengine import *


connect('gestionservicios')


class Notificacion(Document):
	"""
		Sprint: 1

		Modelo  que representa la 
	configuración de notificación
	en el sistema.

		@author Paulo_Angeles.
	"""
	_id					= ObjectIdField()
	enabled 			= BooleanField()
	createdAt 			= DateTimeField()
	updatedAt 			= DateTimeField()
	hashId 				= StringField()
	usuarioCreador 		= ObjectIdField()
	serverName	 		= StringField()
	defaultEmail 		= StringField()
	smtpUser 			= StringField()
	smtpPass 			= StringField()
	smtpPort 			= StringField()
	smtpUsaSSl 			= BooleanField()
	smtpTextoHtml 		= StringField()
	defaultMessage 		= StringField()

