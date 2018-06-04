from mongoengine import *


connect('gestionservicios')


class Cliente(Document):
	enabled = BooleanField()
	createdAt = DateTimeField()
	updatedAt = DateTimeField()
	hashId = StringField()
	usuarioCreador = ObjectIdField()
	nombreContacto = StringField()
	razonSocial = StringField()
	nombreComercial = StringField()
	direccion = StringField()
	telefono = StringField()
	email = StringField()
	password = StringField()
