from mongoengine import *
from .rol import Rol


connect('gestionservicios')


class Usuario(Document):
	enabled = BooleanField()
	createdAt = DateTimeField()
	updatedAt = DateTimeField()
	hashId = StringField()
	usuarioCreador = ObjectIdField()
	nombre = StringField()
	email = StringField()
	telefono = StringField()
	imagenPerfil = ObjectIdField()
	nickname = StringField()
	password = StringField()
	rol_id = ObjectIdField()
