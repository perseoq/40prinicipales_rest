from backend.vendors.shemas import marsh

class CantanteEsquema(marsh.Schema):
    class Meta:
        fields = ('id', 'artista', 'pais')

class CancionEsquema(marsh.Schema):
    class Meta:
        fields = ('id', 'cancion', 'cantante')


cantante_schema = CantanteEsquema()
cantantes_schema = CantanteEsquema(many=True)

cancion_schema = CancionEsquema()
canciones_schema = CancionEsquema(many=True)
