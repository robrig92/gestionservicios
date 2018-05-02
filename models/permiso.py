from mongoengine import *


connect('gestionservicios')


class Permiso(Document):
	enabled = BooleanField()
	descripcion = StringField()
	permiso = StringField()
