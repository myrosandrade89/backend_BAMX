from rest_framework import serializers
from comunidades.models import Comunidad

class ComunidadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comunidad
        fields = ['url', 'id', 'nombre', 'clave_sae']