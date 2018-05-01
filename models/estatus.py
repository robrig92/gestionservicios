from mongoengine import *


connect('gestionservicios')


class Estatus(Document):
    enabled = BooleanField()
    descripcion = StringField()
    nombre = StringField()
