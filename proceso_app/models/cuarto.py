from django.db import models
from proceso_app.models.dormitorio import Dormitorio


# Create your models here.

class Cuarto(models.Model):
    codigo = models.CharField(max_length=50, verbose_name="Cuarto", unique=True, primary_key=True)
    capacidad = models.IntegerField(verbose_name="capacidad")
    ocupacion = models.IntegerField(default=0,verbose_name="ocupacion")
    dormitorioID = models.ForeignKey(Dormitorio, verbose_name="dormitorio", on_delete=models.DO_NOTHING, related_name='cuartos')

    def __str__(self):
        return self.codigo