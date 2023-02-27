from comunidades.models import Comunidad
from comunidades.serializers import ComunidadSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.

class ComunidadViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comunidades to be viewed or edited
    """
    queryset = Comunidad.objects.all().order_by('fecha_modificacion')
    serializer_class = ComunidadSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['patch'])
    def increment_estacion(self, request, pk=None):
        comunidad = self.get_object()
        try:
            if 'descripcion' in request.data and comunidad.num_estacion == 0:
                comunidad.descripcion = request.data['descripcion']
            comunidad.num_estacion += 1
            comunidad.save()
            return Response({'status': 'estación actualizada'})
        except ValueError as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)