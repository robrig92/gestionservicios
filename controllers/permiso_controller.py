from ..models.permiso import Permiso
from flask import Blueprint, request


permiso = Blueprint('permiso', __name__)
"""
    Controlador de modelo Permiso.

    @author Roberto_Padilla
"""
@permiso.route('/', methods=['GET'])
def index():
    """
        Sprint 1:

        Método index recupera todos los documentos de
        permiso del amacenamiento de datos.

        @author Roberto_Padilla
    """
    permiso = Permiso.objects()
    return permiso.to_json()

@permiso.route('/<id>', methods=['GET'])
def show(id):
	"""
		Sprint 1:

		Este método recupera un documento permiso por medio
		de su id.

		@author Roberto_Padilla
	"""
	permiso = Permiso.objects(id=id)
	return permiso.to_json()

@permiso.route('/', methods=['POST'])
def store():
	"""
		Sprint 1:

		Este método almacena un documento en la
		base de datos.

		@author Roberto_Padilla
	"""
	if request.form.get('enabled') == '1':
		enabled = True
	else:
		enabled = False
	permiso = Permiso()
	permiso.enabled = enabled
	permiso.permiso = request.form.get('permiso', 'Nombre por defecto')
	permiso.descripcion = request.form.get('descripcion', 'Descripcion por defecto')
	permiso.save()
	return 'success'

@permiso.route('/<id>', methods=['PATCH'])
def patch(id):
	"""
		Sprint 1:

		Este método actualiza la información de un documento
		en la base de datos identificándolo por medio de
		su id.

		@author Roberto_Padilla
	"""
	permiso = Permiso.objects.get(id=id)
	if request.form['enabled'] == '1':
		enabled = True
	else:
		enabled = False
	permiso.enabled = enabled
	permiso.permiso = request.form.get('permiso', 'VALOR POR DEFECTO')
	permiso.descripcion = request.form.get('descripcion', 'Descripción por defecto')
	permiso.save()
	return 'success'
