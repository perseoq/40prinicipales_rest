from flask import Blueprint, jsonify, request
from backend.models.modelos import Canciones, Cantantes
from backend.models.esquemas import cancion_schema, canciones_schema
from backend.vendors.database import db

song = Blueprint('song', __name__)

@song.route('/song/add',  methods=['POST'])
def add_song():
    nombre = request.json['cancion']
    cantante = request.json['cantante']
    # asignamos variable cancion a la tabla
    cancion = Canciones(cancion=nombre, id_cantante=cantante)
    # agregamos los cambios al stage
    db.session.add(cancion)
    # guardamos los cambios
    db.session.commit()
    # nos va a regresar la variable cancion que viene de la tabla
    return cancion_schema.jsonify(cancion)

@song.route('/song', methods=['GET'])
def ver_canciones():
    canciones = Canciones.query.all()
    get_songs = canciones_schema.dump(canciones)
    return jsonify(get_songs)

@song.route('/song/edit/<int:id>', methods=['PUT'])
def editar_cancion(id):
    get_cancion = Canciones.query.get(id)
    get_cancion.cancion = request.json['cancion']
    get_cancion.id_cantante = request.json['cantante']
    db.session.commit()
    return cancion_schema.jsonify(get_cancion)

@song.route('/song/delete/<int:id>', methods=['DELETE'])
def borrar_cancion(id):
    get_cancion = Canciones.query.get(id)
    db.session.delete(get_cancion)
    db.session.commit()
    return 'cancion eliminado'