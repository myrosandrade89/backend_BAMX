from rest_framework import viewsets, permissions
from turnos.models import Turno
from turnos.serializers import TurnoSerializer

class TurnoViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows turnos to be viewed or edited.
  """
  queryset = Turno.objects.all().order_by('numero')
  serializer_class = TurnoSerializer
  permission_classes = [permissions.IsAuthenticated]