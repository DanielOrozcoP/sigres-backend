from proceso_app.models.cuarto import Cuarto 
from proceso_app.models.estudiante import Estudiante
from proceso_app.models.sede import Sede
from proceso_app.serializers.cuarto import CuartoSerializer
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.db.models import F, Q, Count
from django.core.exceptions import ValidationError

# Create your views here.

@api_view(['GET'])
def get_cuarto_free(request):
    """
    Obtiene los cuartos disponibles según los criterios especificados.
    
    Query Params:
        sede_id (opcional): Filtrar por sede específica
        capacidad_min (opcional): Capacidad mínima requerida
        capacidad_max (opcional): Capacidad máxima requerida
        edificio_id (opcional): Filtrar por edificio específico
        ordenar_por (opcional): Campo por el cual ordenar ('capacidad', 'ocupacion')
        
    Returns:
        JsonResponse con la lista de cuartos disponibles y metadata
    """
    try:
        # Obtener parámetros de consulta
        sede_id = request.GET.get('sede_id')
        capacidad_min = request.GET.get('capacidad_min')
        capacidad_max = request.GET.get('capacidad_max')
        edificio_id = request.GET.get('edificio_id')
        ordenar_por = request.GET.get('ordenar_por', 'capacidad')

        # Construir query base
        query = Q(ocupacion__lt=F('capacidad'))  # Cuartos con espacio disponible

        # Aplicar filtros según parámetros
        if sede_id:
            query &= Q(dormitorioID__edificioID__sedeID__codigo=sede_id)
        
        if edificio_id:
            query &= Q(dormitorioID__edificioID__codigo=edificio_id)
        
        if capacidad_min:
            query &= Q(capacidad__gte=int(capacidad_min))
            
        if capacidad_max:
            query &= Q(capacidad__lte=int(capacidad_max))

        # Definir orden
        order_options = {
            'capacidad': 'capacidad',
            '-capacidad': '-capacidad',
            'ocupacion': 'ocupacion',
            '-ocupacion': '-ocupacion',
            'disponibilidad': F('capacidad') - F('ocupacion'),
            '-disponibilidad': -(F('capacidad') - F('ocupacion'))
        }
        
        order_by = order_options.get(ordenar_por, 'capacidad')

        # Obtener cuartos
        cuartos_disponibles = (
            Cuarto.objects.filter(query)
            .select_related('dormitorioID__edificioID__sedeID')
            .order_by(order_by)
        )

        # Serializar resultados
        serializer = CuartoSerializer(cuartos_disponibles, many=True)

        return JsonResponse({
            'metadata': {
                'total_cuartos': cuartos_disponibles.count(),
                'filtros_aplicados': {
                    'sede_id': sede_id,
                    'edificio_id': edificio_id,
                    'capacidad_min': capacidad_min,
                    'capacidad_max': capacidad_max,
                    'ordenar_por': ordenar_por
                }
            },
            'cuartos_disponibles': serializer.data
        })

    except Exception as e:
        return JsonResponse({
            'error': str(e)
        }, status=500)

@api_view(['GET'])
def asignar_cuarto(request):
    """
    Encuentra un cuarto disponible para asignar basado en los criterios del estudiante.
    
    Query Params:
        estudiante_id: ID del estudiante
        sede_id: ID de la sede (opcional)
    
    Returns:
        JsonResponse con el cuarto sugerido para asignación
    """
    try:
        estudiante_id = request.GET.get('estudiante_id')
        sede_id = request.GET.get('sede_id')

        if not estudiante_id:
            return JsonResponse({
                'error': 'Se requiere el ID del estudiante'
            }, status=400)

        try:
            estudiante = Estudiante.objects.get(carnet_identidad=estudiante_id)
        except Estudiante.DoesNotExist:
            return JsonResponse({
                'error': 'Estudiante no encontrado'
            }, status=404)

        # Construir query base
        query = Q(ocupacion__lt=F('capacidad'))  # Cuartos con espacio disponible

        # Si se especifica sede, filtrar por ella
        if sede_id:
            query &= Q(dormitorioID__edificioID__sedeID__codigo=sede_id)

        # Priorizar cuartos
        cuarto_sugerido = (
            Cuarto.objects.filter(query)
            .annotate(
                estudiantes_misma_carrera=Count(
                    'estudiantes',
                    filter=Q(estudiantes__carrera=estudiante.carrera)
                ),
                estudiantes_misma_facultad=Count(
                    'estudiantes',
                    filter=Q(estudiantes__facultad=estudiante.facultad)
                )
            )
            .order_by(
                '-estudiantes_misma_carrera',
                '-estudiantes_misma_facultad',
                'ocupacion'
            )
            .first()
        )

        if not cuarto_sugerido:
            return JsonResponse({
                'message': 'No hay cuartos disponibles con los criterios especificados'
            }, status=404)

        serializer = CuartoSerializer(cuarto_sugerido)
        return JsonResponse({
            'cuarto_sugerido': serializer.data,
            'mensaje': 'Cuarto disponible para asignación'
        })

    except Exception as e:
        return JsonResponse({
            'error': str(e)
        }, status=500)