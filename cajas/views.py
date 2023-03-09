from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from cajas.models import Caja
from cajas.serializers import CajaSerializer, CajaIDSerializer
from turnos.models import Turno


# Create your views here.

class CajaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows cajas to be viewed or edited
    """
    queryset = Caja.objects.all().order_by('nombre')
    serializer_class = CajaSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['patch'], serializer_class=CajaIDSerializer)
    def siguiente_turno(self, request, pk=None):
        caja = self.get_object()
        try:
            if caja.user == None:
                return Response({'error': 'caja sin usuario'},status=status.HTTP_400_BAD_REQUEST)
            turno = Turno.objects.filter(caja=caja, en_atencion=True).order_by('numero').first()
            if turno != None:
                turno.delete()
            
            turno = Turno.objects.filter(en_atencion=False).order_by('numero').first()

            if turno == None:
                return Response({'status': f'no hay turnos pendientes'},status=status.HTTP_200_OK)

            turno.caja = caja
            turno.en_atencion = True
            turno.save()
            return Response({'status': f'turno {turno.numero} en atención'},status=status.HTTP_200_OK)
        except ValueError as e:
          return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            