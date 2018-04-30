from ..models.rol import Rol
from bson import ObjectId
import datetime


class RolController():
	"""
	 Controlador de modelo Rol.
	"""
	def index(self):
		roles = Rol.objects()
		return roles.to_json()

	def show(self, hashId):
		roles = Rol.objects(hashId=hashId)
		return roles.to_json()

	def store(self, request):
		if request.form['enabled'] == 1:
			enabled = True
		else:
			enabled = False
		rol = Rol()
		rol.enabled = enabled
		rol.createdAt = datetime.datetime.utcnow()
		rol.updatedAt = datetime.datetime.utcnow()
		rol.hashId = 'sdfhsdjkhf234234@#$@#dsfsd'
		rol.usuarioCreador = ObjectId(request.form['usuarioCreador'])
		rol.nombre = request.form['nombre']
		rol.save()
		return 'success'

	def patch(self, hashId, request):
		rol = Rol.objects(hashId=hashId)
		if request.form['enabled'] == 1:
			enabled = True
		else:
			enabled =  False
		rol.enabled = enabled
		rol.updatedAt = datetime.datetime.utcnow()
		rol.nombre = request.form['nombre']
		rol.save()
		return 'success'
