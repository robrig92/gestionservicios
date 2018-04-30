from mongoengine import *


connect('gestionservicios')


class Rol(Document):
	enabled = BooleanField()
	createdAt = DateTimeField()
	updatedAt = DateTimeField()
	hashId = StringField()
	usuarioCreador = ObjectIdField()
	nombre = StringField()
