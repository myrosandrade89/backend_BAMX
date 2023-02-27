from django.db import models

# Create your models here.
class Caja(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Cajas'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre