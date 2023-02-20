from rest_framework import serializers
from comunidades.models import Comunidad

class ComunidadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comunidad
        fields = ['url', 'id', 'nombre', 'representante', 'descripcion', 'num_estacion', 'fecha_modificacion']