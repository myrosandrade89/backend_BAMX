from django.db import models

# Create your models here.
class Comunidad(models.Model):
    nombre = models.CharField(max_length=100)
    clave_sae =  models.CharField(max_length=100, unique=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Comunidades'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre