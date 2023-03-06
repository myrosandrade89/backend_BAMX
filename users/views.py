from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model as User
from users.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
