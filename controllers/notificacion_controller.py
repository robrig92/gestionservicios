from flask import Blueprint, request
from ..models.notificacion import Notificacion
from ..utils.StringUtils import StringUtils
import datetime
import time
from bson import ObjectId


notificacion = Blueprint('notificacion', __name__)
"""	    

	Controller encargado de las operaciones relacionadas
con la configuración de notificaciones.

    @author Paulo_Angeles.
"""
@notificacion.route('', methods=['GET'])
def list():
	"""
		Sprint: 1.

			Método encargado de listar todos
		las configuraciones de notificación existentes
		en el sistema

		@author Paulo_Angeles.
	"""
	print("REQUEST GET. List configuración notificación.")
	notificaciones = Notificacion.objects()
	return notificaciones.to_json()

@notificacion.route('/<hashId>', methods=['GET'])
def get( hashId ):
	"""
		Sprint: 1.

			Método encargado de obtener una
		configuracion de notificación determinada
		mediante su campo hash_id.

		@author Paulo_Angeles.
	"""
	print("REQUEST GET. Get configuración notificación hashId = " + hashId )
	notificacion = Notificacion.objects.get(hashId=hashId)
	return notificacion.to_json()

@notificacion.route('', methods=['POST'])
def save( ):

	"""
		Sprint: 1.

			Método encargado de persistir una
		configuración de notificación en el sitema.

		@author Paulo_Angeles.
	"""
	print("REQUEST POST. Create configuración notificación.")
	notificacion 					= Notificacion()
	notificacion.enabled 			= True
	notificacion.createdAt 			= datetime.datetime.utcnow()
	notificacion.updatedAt 			= datetime.datetime.utcnow()
	notificacion.hashId 			= StringUtils.randomHash();
	notificacion.usuarioCreador 	= ObjectId(request.form.get('usuarioCreador', '5adf9abc30c9451b476ee260' ) )
	notificacion.serverName	 		= request.form.get( 'server_name'			, 'Server name por defecto' )
	notificacion.defaultEmail 		= request.form.get( 'default_email'			, 'Default email por defecto' )
	notificacion.smtpUser 			= request.form.get( 'smtp_user'				, 'SMTP USER por defecto' )
	notificacion.smtpPass 			= request.form.get( 'smtp_pass'				, 'SMTP PASS por defecto' )
	notificacion.smtpPort 			= request.form.get( 'smtp_port'				, 'SMTP PORT por defecto' )
	notificacion.smtpUsaSSl 		= request.form.get( 'smpt_usa_ssl'			, True )
	notificacion.smtpTextoHtml 		= request.form.get( 'smpt_texto_html'		, 'SMPT TEXTO HTML por defecto' )
	notificacion.defaultMessage 	= request.form.get( 'smpt_default_message'	, 'SMPT DEFAULT MESSAGE por defecto' )
	notificacion.save()
	return 'success create'

@notificacion.route('/<hashId>', methods=['PATCH'])
def update( hashId ):
	"""
		Sprint: 1.

			Método encargado de actualizar una
		configuración de notificación en el sitema.

		@author Paulo_Angeles.
	"""
	print("REQUEST PATCH. Update configuración notificación hashId = " + hashId )
	notificacion 					= Notificacion.objects.get(hashId=hashId)
	notificacion.updatedAt 			= datetime.datetime.utcnow()
	notificacion.serverName	 		= request.form.get( 'server_name'			, 'Server name por defecto' + str(time.time() ) )
	notificacion.defaultEmail 		= request.form.get( 'default_email'				, 'Default email por defecto' + str(time.time() ) )
	notificacion.smtpUser 			= request.form.get( 'smtp_user'					, 'SMTP USER por defecto' + str(time.time() ) )
	notificacion.smtpPass 			= request.form.get( 'smtp_pass'					, 'SMTP PASS por defecto' + str(time.time() ) )
	notificacion.smtpPort 			= request.form.get( 'smtp_port'					, 'SMTP PORT por defecto' + str(time.time() ) )
	notificacion.smtpUsaSSl 		= request.form.get( 'smpt_usa_ssl'				, True )
	notificacion.smtpTextoHtml 		= request.form.get( 'smpt_texto_html'			, 'SMPT TEXTO HTML por defecto' + str(time.time() ) )
	notificacion.defaultMessage 	= request.form.get( 'smpt_default_message'		, 'SMPT DEFAULT MESSAGE por defecto' + str(time.time() ) )
	notificacion.save()
	return 'success update'
