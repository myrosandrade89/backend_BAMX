from cajas.models import Caja
from cajas.serializers import CajaSerializer
from rest_framework import viewsets, permissions


# Create your views here.

class CajaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cajas to be viewed or edited
    """
    queryset = Caja.objects.all().order_by('nombre')
    serializer_class = CajaSerializer
    permission_classes = [permissions.IsAuthenticated]