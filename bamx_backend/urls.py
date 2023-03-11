from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter
from comunidades.views import ComunidadViewSet
from turnos.views import TurnoViewSet
from cajas.views import CajaViewSet
from users.views import UserViewSet
from users.views import CurrentUserView
from link.views import LinkViewSet


# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'comunidades', ComunidadViewSet,basename="comunidad")
router.register(r'turnos', TurnoViewSet,basename="turno")
router.register(r'cajas', CajaViewSet,basename="caja")
router.register(r'users', UserViewSet,basename="user")
router.register(r'link', LinkViewSet,basename="link")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('users/my', CurrentUserView.as_view()),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]