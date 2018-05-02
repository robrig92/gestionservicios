from mongoengine import *

connect('gestionservicios')


class Marca(Document):
	enabled = BooleanField()
	createdAt = DateTimeField()
	updatedAt = DateTimeField()
	usuarioCreador = ObjectIdField()
	marca = StringField()
