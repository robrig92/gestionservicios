from ..models.usuario import Usuario

class UsuarioController():
	"""
	 Controlador de modelo usuario
	"""
	def index(self):
		return Usuario.objects().to_json()
