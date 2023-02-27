from django.urls import path, include
from rest_framework.routers import DefaultRouter
from comunidades.views import ComunidadViewSet
from turnos.views import TurnoViewSet
from cajas.views import CajaViewSet



# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'comunidades', ComunidadViewSet,basename="comunidad")
router.register(r'turnos', TurnoViewSet,basename="turno")
router.register(r'cajas', CajaViewSet,basename="caja")

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),

]