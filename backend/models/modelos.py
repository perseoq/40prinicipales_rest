from backend.vendors.database import db


class Cantantes(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    artista = db.Column(db.String(300), nullable=False)
    pais = db.Column(db.String(300), nullable=False)
    cancion = db.relationship('Canciones', backref='Cantantes')

    def __init__(self, artista, pais):
        self.artista = artista
        self.pais = pais

class Canciones(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    cancion = db.Column(db.String(300), nullable=False)
    id_cantante = db.Column(db.Integer(), db.ForeignKey('cantantes.id'))

    def __init__(self, cancion, id_cantante):
        self.cancion = cancion
        self.id_cantante = id_cantante