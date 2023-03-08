from link.models import Link
from link.serializers import LinkSerializer
from rest_framework import viewsets, permissions


# Create your views here.

class LinkViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comunidades to be viewed or edited
    """
    queryset = Link.objects.all().order_by('liga')
    serializer_class = LinkSerializer
    permission_classes = [permissions.IsAuthenticated]