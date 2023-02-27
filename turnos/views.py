from turnos.models import Turno
from turnos.serializers import TurnoSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response



# Create your views here.

class TurnoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Turnos to be viewed or edited
    """
    queryset = Turno.objects.all().order_by('-numero')
    serializer_class = TurnoSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['patch'])
    def cambio_estado(self, request, pk=None):
        turno = self.get_object
        try:
            if not turno.en_atencion:
                turno.en_atencion = True
                turno.caja = request.data['caja']
                turno.save()
                return Response({'status': 'turno en atención'},status=status.HTTP_200_OK)

            else:
                turno.delete()
            return Response({'status': 'turno eliminado'},status=status.HTTP_200_OK)
        except ValueError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)