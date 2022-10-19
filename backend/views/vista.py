from flask import Blueprint, render_template
from backend.models.modelos import Canciones, Cantantes
from backend.models.esquemas import cancion_schema, canciones_schema
from backend.vendors.database import db

view = Blueprint('view', __name__)

@view.route('/view')
def vista():
    canciones = db.session.query(Cantantes, Canciones).join(Canciones, Canciones.id_cantante==Cantantes.id).all()
    return render_template('vista.html', data=canciones)