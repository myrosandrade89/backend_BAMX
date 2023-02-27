from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from cajas.models import Caja
from turnos.models import Turno
from turnos.serializers import TurnoSerializer, CambioTurnoSerializer

class TurnoViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows turnos to be viewed or edited.
  """
  queryset = Turno.objects.all().order_by('numero')
  serializer_class = TurnoSerializer
  permission_classes = [permissions.IsAuthenticated]

  @action(detail=True, methods=['patch'], serializer_class=CambioTurnoSerializer)
  def cambio_estado(self, request, pk=None):
    turno = self.get_object()
    try:
      serializer = CambioTurnoSerializer(data=request.data)
      if not turno.en_atencion:
        if serializer.is_valid():
          turno.caja = serializer.validated_data['caja']
          turno.en_atencion = True
          turno.save()
          return Response({'status': 'turno en atención'},status=status.HTTP_200_OK)
        else:
          return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
      else:
        turno.delete()
        return Response({'status': 'turno eliminado'},status=status.HTTP_200_OK)
    except ValueError as e:
      return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)