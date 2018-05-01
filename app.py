from mongoengine import *
from flask import Flask, request
from .controllers.rol_controller import rol
from .controllers.cliente_controller import cliente
from .controllers.servicio_controller import servicio
from .controllers.prioridad_controller import prioridad
from .controllers.notificacion_controller import notificacion
from .controllers.usuario_controller import UsuarioController
from .controllers.tipoDispositivo_controller import tipoDispositivo
from .middleware.HTTPMethodOverrideMiddleware import HTTPMethodOverrideMiddleware

app = Flask(__name__)
app.wsgi_app = HTTPMethodOverrideMiddleware(app.wsgi_app)

app.register_blueprint( cliente 			, url_prefix='/api/cliente')
app.register_blueprint( tipoDispositivo 	, url_prefix='/api/tipodispositivo')
app.register_blueprint( servicio 			, url_prefix='/api/servicio')
app.register_blueprint( notificacion 		, url_prefix='/api/notificacion')
app.register_blueprint( prioridad 			, url_prefix='/api/prioridad')
app.register_blueprint( rol, url_prefix='/api/rol' )
