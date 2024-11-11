from proceso_app.models.cuarto import Cuarto
from django.db.models import F

def get_cuartos_free():
    cuartos_free = Cuarto.objects.annotate(disponibilidad=F('capacidad')-F('ocupacion')).filter(disponibilidad__gt=0).values('codigo','disponibilidad','dormitorioID')
    return cuartos_free