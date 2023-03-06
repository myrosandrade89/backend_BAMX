from rest_framework import serializers
from cajas.models import Caja

class CajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Caja
        fields = [ 'id', 'nombre', 'user']