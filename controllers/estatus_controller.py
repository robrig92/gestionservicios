from ..models.estatus import Estatus
from flask import Blueprint, request


estatus = Blueprint('rol', __name__)
"""
    Controlador de modelo Estatus.

    @author Roberto_Padilla
"""
@estatus.route('/', methods=['GET'])
def index():
    """
        Sprint 1:

        Método index recupera todos los documentos de
        estatus del amacenamiento de datos.

        @author Roberto_Padilla
    """
    estatus = Estatus.objects()
    return estatus.to_json()

@estatus.route('/<hashId>', methods=['GET'])
def show(hashId):
	"""
		Sprint 1:

		Este método recupera un documento estatus por medio
		de su hashId.

		@author Roberto_Padilla
	"""
	estatus = Estatus.objects(hashId=hashId)
	return estatus.to_json()

@estatus.route('/', methods=['POST'])
def store(request):
	"""
		Sprint 1:

		Este método almacena un documento en la
		base de datos.

		@author Roberto_Padilla
	"""
	if request.form['enabled'] == 1:
		enabled = True
	else:
		enabled = False
	estatus = Estatus()
	estatus.enabled = enabled
	estatus.nombre = request.form.get('nombre', 'Nombre por defecto')
    estatus.descripcion = request.form.get('descripcion', 'Descripcion por defecto')
    estatus.save()
	return 'success'

@estatus.route('/<hashId>', methods=['PATCH'])
def patch(hashId, request):
	"""
		Sprint 1:

		Este método actualiza la información de un documento
		en la base de datos identificándolo por medio de
		su hashId.

		@author Roberto_Padilla
	"""
	estatus = Estatus.objects.get(hashId=hashId)
	if request.form.get('nombre', 1) == 1:
		enabled = True
	else:
		enabled =  False
	estatus.enabled = enabled
	estatus.nombre = request.form.get('nombre', 'VALOR POR DEFECTO')
    estatus.descripcion = request.form.get('descripcion', 'Descripción por defecto')
    estatus.save()
	return 'success'
