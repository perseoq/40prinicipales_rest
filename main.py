from flask import Flask
from backend.controllers.config import RestApiConfig
from backend.vendors.database import db
from backend.vendors.shemas import marsh

api = Flask(__name__)

# Importamos todas las configuraciones

api.config.from_object(RestApiConfig)
db.init_app(api)
marsh.init_app(api)

# Importamos los blueprints

from backend.views.cantantes import singer
api.register_blueprint(singer)

from backend.views.canciones import song
api.register_blueprint(song)

from backend.views.vista import view
api.register_blueprint(view)
# Se crean todas las bases de datos

with api.app_context():
    db.create_all()

if __name__=='__main__':
    api.run(debug=True, port=6001)