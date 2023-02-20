from django.db import models

# Create your models here.
class Comunidad(models.Model):
    nombre = models.CharField(max_length=100)
    representante =  models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500, blank=True, default='')
    num_estacion = models.IntegerField(default=0)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
        NUM_LIMITE_ESTACIONES = 5
        if self.num_estacion > NUM_LIMITE_ESTACIONES:
            self.num_estacion = 0
        if self.num_estacion == 0:
            self.descripcion = ''
        if self.num_estacion == 1 and self.descripcion == '':
            raise ValueError('La comunidad debe tener una descipción')
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plurar = 'Comunidades'
        ordering = ['fecha_modificacion']