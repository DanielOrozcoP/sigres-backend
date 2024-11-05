from django.db import models
from proceso_app.models.sede import Sede


# Create your models here.

class Edificio(models.Model):
    codigo = models.CharField(max_length=15, verbose_name="codigo", unique=True, primary_key=True)
    sexo = models.BooleanField(null=True, verbose_name="sexo")
    sedeID = models.ForeignKey(Sede, on_delete=models.DO_NOTHING, verbose_name='sede', related_name='edificios')

    def __str__(self):
        return self.codigo
