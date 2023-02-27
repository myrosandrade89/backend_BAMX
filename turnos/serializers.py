from rest_framework import serializers
from turnos.models import Turno

class TurnoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Turno
        fields = ['url', 'id', 'numero', 'comunidad', 'caja', 'en_atencion']