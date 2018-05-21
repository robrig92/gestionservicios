from mongoengine import *
from flask_cors import CORS
from flask import Flask, request
from .controllers.rol_controller import rol
from .controllers.folio_controller import folio
from .controllers.marca_controller import marca
from .controllers.cliente_controller import cliente
from .controllers.estatus_controller import estatus
from .controllers.permiso_controller import permiso
from .controllers.usuario_controller import usuario
from .controllers.servicio_controller import servicio
from .controllers.prioridad_controller import prioridad
from .controllers.notificacion_controller import notificacion
from .controllers.tipoDispositivo_controller import tipoDispositivo
from .middleware.HTTPMethodOverrideMiddleware import HTTPMethodOverrideMiddleware

app = Flask(__name__)
CORS(app)
app.wsgi_app = HTTPMethodOverrideMiddleware(app.wsgi_app)

app.register_blueprint(cliente 			, url_prefix='/api/cliente')
app.register_blueprint(tipoDispositivo 	, url_prefix='/api/tipodispositivo')
app.register_blueprint(servicio 			, url_prefix='/api/servicio')
app.register_blueprint(notificacion 		, url_prefix='/api/notificacion')
app.register_blueprint(prioridad 			, url_prefix='/api/prioridad')
app.register_blueprint(rol, url_prefix='/api/rol')
app.register_blueprint(folio, url_prefix='/api/folio')
app.register_blueprint(marca, url_prefix='/api/marca')
app.register_blueprint(estatus, url_prefix='/api/estatus')
app.register_blueprint(permiso, url_prefix='/api/permiso')
app.register_blueprint(usuario, url_prefix='/api/usuario')
