from django.db import models
from comunidades import Comunidad
from cajas import Caja


# Create your models here.
class Turno(models.Model):
    numero = models.IntegerField()
    comunidad = models.ForeignKey(Comunidad, on_delete=models.CASCADE, related_name='turnos', unique=True)
    caja =  models.ForeignKey(Caja, on_delete=models.CASCADE, related_name='turnos', unique=True, null=True, blank=True)
    en_atencion = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.en_atencion and (self.caja == None or self.caja == ''):
            raise ValueError('No se puede guardar un turno en atención sin caja')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Turnos'
        ordering = ['-numero']