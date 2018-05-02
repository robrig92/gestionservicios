from mongoengine import *


connect('gestionservicios')

class Folio(Document):
	enabled = BooleanField()
	createdAt = DateTimeField()
	updatedAt = DateTimeField()
	hashId = StringField()
	usuarioCreador = ObjectIdField()
	cliente_id = ObjectIdField()
	servicio_id = ObjectIdField()
	asignadoA = ObjectIdField()
	prioridad_id = ObjectIdField()
	cotizacion = DecimalField()
	total = DecimalField()
	fechaAbre = DateTimeField()
	fechaCierre = DateTimeField()
	estatus_id = ObjectIdField()
	numeroSerie = StringField()
	tipoDispositivo_id = ObjectIdField()
	marca_id = ObjectIdField()
	observaciones = StringField()
