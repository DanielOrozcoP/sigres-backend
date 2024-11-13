from proceso_app.models.cuarto import Cuarto
from proceso_app.serializers.cuarto import CuartoSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.db.models import ExpressionWrapper, F
from servicios_app import utils

# Create your views here.

@api_view(['GET',])
def get_cuarto_free(request):
    if request.method == 'GET':
        cuarto_free = utils.get_cuartos_free()
        data = {'cuartos_free': list(cuarto_free)}
        return JsonResponse(data)
    
@api_view(['GET',])
def asignar_cuarto(request):
    if request.method == 'GET':
        cuarto_free = utils.get_cuartos_free()
        data = {'cuartos_free': list(cuarto_free)}
        return JsonResponse(data)