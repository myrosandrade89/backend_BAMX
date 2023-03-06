from rest_framework import serializers
from turnos.models import Turno

class TurnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turno
        fields = ['id', 'numero', 'comunidad', 'caja', 'en_atencion']
