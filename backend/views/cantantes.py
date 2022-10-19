from flask import Blueprint, jsonify, request
from backend.models.modelos import Cantantes
from backend.models.esquemas import cantante_schema, cantantes_schema
from backend.vendors.database import db

singer = Blueprint('singer', __name__)


@singer.route('/singer/add',  methods=['POST'])
def add_singer():
    nombre = request.json['artista']
    pais = request.json['pais']
    # asignamos variable cantante a la tabla
    cantante = Cantantes(artista=nombre, pais=pais)
    # agregamos los cambios al stage
    db.session.add(cantante)
    # guardamos los cambios
    db.session.commit()
    # nos va a regresar la variable cantante que viene de la tabla
    return cantante_schema.jsonify(cantante)

@singer.route('/singer', methods=['GET'])
def ver_cantantes():
    cantantes = Cantantes.query.all()
    get_singers = cantantes_schema.dump(cantantes)
    return jsonify(get_singers)




@singer.route('/singer/edit/<int:id>', methods=['PUT'])
def editar_cantante(id):
    get_cantante = Cantantes.query.get(id)
    get_cantante.artista = request.json['artista']
    get_cantante.pais = request.json['pais']
    db.session.commit()
    return cantante_schema.jsonify(get_cantante)

@singer.route('/singer/delete/<int:id>', methods=['DELETE'])
def borrar_cantante(id):
    get_cantante = Cantantes.query.get(id)
    db.session.delete(get_cantante)
    db.session.commit()
    return 'Cantante eliminado'
