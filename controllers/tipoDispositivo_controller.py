from flask import Blueprint, request
from ..models.tipoDispositivo import TipoDispositivo
from ..utils.StringUtils import StringUtils
import datetime
import time
from bson import ObjectId


tipoDispositivo = Blueprint('tipoDispositivo', __name__)

@tipoDispositivo.route('', methods=['GET'])
def list():
	print("REQUEST GET. List tipo dispositivo.")
	tiposDispositivo = TipoDispositivo.objects()
	return tiposDispositivo.to_json()

@tipoDispositivo.route('/<hashId>', methods=['GET'])
def detail( hashId ):
	print("REQUEST GET. Detail tipo dispositivo hashId = " + hashId )
	tipoDispositivo = TipoDispositivo.objects.get(hashId=hashId)
	return tipoDispositivo.to_json()

@tipoDispositivo.route('', methods=['POST'])
def save( ):
	print("REQUEST POST. Create tipo dispositivo.")
	tipoDispositivo 					= TipoDispositivo()
	tipoDispositivo.enabled 			= True
	tipoDispositivo.createdAt 			= datetime.datetime.utcnow()
	tipoDispositivo.updatedAt 			= datetime.datetime.utcnow()
	tipoDispositivo.hashId 				= StringUtils.randomHash();
	tipoDispositivo.usuarioCreador 		= ObjectId(request.form.get('usuarioCreador', '5adf9abc30c9451b476ee260' ) )
	tipoDispositivo.tipo 				= request.form.get('tipo',  'Tipo por defecto')
	tipoDispositivo.save()
	return 'success create'

@tipoDispositivo.route('/<hashId>', methods=['PATCH'])
def update( hashId ):
	print("REQUEST PATCH. Update tipo dispositivo hashId = " + hashId )
	tipoDispositivo 					= TipoDispositivo.objects.get(hashId=hashId)
	tipoDispositivo.updatedAt 			= datetime.datetime.utcnow()
	tipoDispositivo.tipo 			 	= request.form.get('tipo',  'Tipo por defecto' + str(time.time()) )
	tipoDispositivo.save()
	return 'success update'
