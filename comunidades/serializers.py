from rest_framework import serializers
from comunidades.models import Comunidad

class ComunidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comunidad
        fields = ['id', 'nombre', 'clave_sae']