from django.db import models
from comunidades.models import Comunidad
from cajas.models import Caja
from rest_framework import serializers


# Create your models here.
class Turno(models.Model):
    numero = models.IntegerField()
    comunidad = models.OneToOneField(Comunidad, on_delete=models.CASCADE, related_name='turno', unique=True)
    caja =  models.OneToOneField(Caja, on_delete=models.CASCADE, related_name='turno', unique=True, null=True, blank=True)
    en_atencion = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.en_atencion and (self.caja == None or self.caja == ''):
            raise serializers.ValidationError({'turno': 'No se puede guardar un turno en atención sin caja'})
        if not self.en_atencion and (self.caja != None and self.caja != ''):
            raise serializers.ValidationError({'turno': 'No se puede guardar un turno no en atención con caja'})
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Turnos'
        ordering = ['numero']

    def __str__(self):
        return self.numero