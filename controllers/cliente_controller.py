from flask import Blueprint, request
from ..models.cliente import Cliente
from ..utils.StringUtils import StringUtils
import datetime
import time
from bson import ObjectId


cliente = Blueprint('cliente', __name__)

@cliente.route('', methods=['GET'])
def list():
	clientes = Cliente.objects()
	return clientes.to_json()

@cliente.route('/<hashId>', methods=['GET'])
def detail( hashId ):
	cliente = Cliente.objects.get(hashId=hashId)
	return cliente.to_json()

@cliente.route('', methods=['POST'])
def save( ):
	cliente = Cliente()
	cliente.enabled 		= True
	cliente.createdAt 		= datetime.datetime.utcnow()
	cliente.updatedAt 		= datetime.datetime.utcnow()
	cliente.hashId 			= StringUtils.randomHash();
	cliente.usuarioCreador 	= ObjectId(request.form.get('usuarioCreador', '5adf9abc30c9451b476ee260' ) )
	cliente.nombreContacto 	= request.form.get('nombre_contacto',  'Nombre por defecto')
	cliente.razonSocial 	= request.form.get('razon_social',  'Razón social por defecto')
	cliente.nombreComercial = request.form.get('nombre_comercial',  'Nombre Comercial por defecto')
	cliente.direccion 		= request.form.get('direccion',  'Dirección por defecto')
	cliente.telefono 		= request.form.get('telefono',  'Teléfono por defecto')
	cliente.email	 		= request.form.get('email',  'Email por defecto')
	cliente.save()

	return 'success create'

@cliente.route('/<hashId>', methods=['PATCH'])
def update( hashId ):
	cliente = Cliente.objects.get(hashId=hashId)
	cliente.updatedAt 		= datetime.datetime.utcnow()
	cliente.nombreContacto 	= request.form.get('nombre_contacto',  'Nombre por defecto' + str(time.time()) )
	cliente.razonSocial 	= request.form.get('razon_social',  'Razón social por defecto' + str(time.time()) )
	cliente.nombreComercial = request.form.get('nombre_comercial',  'Nombre Comercial por defecto' + str(time.time()) )
	cliente.direccion 		= request.form.get('direccion',  'Dirección por defecto' + str(time.time()) )
	cliente.telefono 		= request.form.get('telefono',  'Teléfono por defecto' + str(time.time()) ) 
	cliente.email	 		= request.form.get('email',  'Email por defecto' + str(time.time()) )
	cliente.save()
	return 'success update'
