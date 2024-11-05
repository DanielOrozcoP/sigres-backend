from django.db import models
from django.core.exceptions import ValidationError
from proceso_app.models.cuarto import Cuarto


class Estudiante(models.Model):
    carnet_identidad = models.CharField(max_length=11, verbose_name='Carnet de Identidad', unique=True, primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='nombre')
    apellido = models.CharField(max_length=100, verbose_name='Apellido')
    facultad = models.CharField(max_length=100, verbose_name='Facultad')
    carrera = models.CharField(max_length=100, verbose_name='Carrera')
    ano_academico = models.IntegerField(null=True, verbose_name='Año academico')
    eliminado = models.BooleanField(default=False, verbose_name='Eliminado')
    cuarto = models.ForeignKey(Cuarto, on_delete=models.DO_NOTHING, verbose_name='cuarto', related_name='estudiantes')

    def __str__(self):
        return self.nombre
