from rest_framework import viewsets, permissions, views
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import get_user_model as User
from users.serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User().objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

# View for getting the current user
class CurrentUserView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)