from comunidades.models import Comunidad
from comunidades.serializers import ComunidadSerializer
from rest_framework import viewsets, permissions


# Create your views here.

# Viewset that allows comunidades to be viewed by any user and edited by admins only
class ComunidadViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comunidades to be viewed or edited
    """
    queryset = Comunidad.objects.all().order_by('nombre')
    serializer_class = ComunidadSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            self.permission_classes = [permissions.IsAdminUser]
        return super(self.__class__, self).get_permissions()