from rest_framework import serializers
from link.models import Link

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['id', 'liga', 'fila_inicial']