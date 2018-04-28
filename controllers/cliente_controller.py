from ..models.cliente import Cliente

class ClienteController():
	'Controlador de Modelo cliente'
	def index(self):
		return Cliente.objects()
