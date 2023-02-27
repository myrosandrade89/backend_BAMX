from rest_framework import serializers
from cajas.models import Caja

class CajaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Caja
        fields = ['url', 'id', 'nombre']