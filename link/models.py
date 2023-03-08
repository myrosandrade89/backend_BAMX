from django.db import models
from rest_framework import serializers

# Create your models here.
class Link(models.Model):
    liga = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['liga']

    def __str__(self):
        return self.liga