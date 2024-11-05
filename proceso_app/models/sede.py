from django.db import models


class Sede(models.Model):
    codigo = models.CharField(max_length=15, verbose_name='codigo', unique=True, primary_key=True)
    direccion = models.CharField(max_length=250, verbose_name='direccion')
    nombre = models.CharField(max_length=50, verbose_name='nombre')

    def __str__(self):
        return self.nombre