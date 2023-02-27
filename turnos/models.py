from django.db import models
from comunidades import Comunidad

# Create your models here.
class Turno(models.Model):
    numero = models.IntegerField()
    comunidad = models.ForeignKey(Comunidad, on_delete=models.CASCADE, related_name='turnos', unique=True)
    en_atencion = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Turnos'
        ordering = ['-numero']