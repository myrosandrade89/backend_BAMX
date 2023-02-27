from comunidades.models import Comunidad
from comunidades.serializers import ComunidadSerializer
from rest_framework import viewsets, permissions


# Create your views here.

class ComunidadViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comunidades to be viewed or edited
    """
    queryset = Comunidad.objects.all().order_by('nombre')
    serializer_class = ComunidadSerializer
    permission_classes = [permissions.IsAuthenticated]