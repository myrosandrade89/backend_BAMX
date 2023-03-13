from comunidades.models import Comunidad
from comunidades.serializers import ComunidadSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action


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

    @action(detail=False, methods=['get'])
    def get_comunidad_por_clave_sae(self, request):
        clave_sae = request.query_params.get('clave_sae', None)
        if clave_sae is not None:
            try:
                comunidad = Comunidad.objects.get(clave_sae=clave_sae)
                serializer = ComunidadSerializer(comunidad)
                return Response(serializer.data)
            except Comunidad.DoesNotExist:
                return Response({'error': 'clave sae no encontrada'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'clave sae no especificada'}, status=status.HTTP_400_BAD_REQUEST)