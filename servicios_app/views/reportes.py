from servicios_app.serializers.reportes import Rep_Total_by_Sede_Serializer, Rep_Total_Serializer
from rest_framework import generics
from django.db.models import Count
from control_acceso_app.auth.permissions import IsEspecialista
from proceso_app.models import sede, edificio, dormitorio,cuarto,estudiante
from rest_framework.response import Response

class Rep_Total_by_Sede(generics.ListAPIView):
    """
    Retorna el total de edificio, dormitorio, cuarto y estudiantes, por sedes.
        {
            codigo, nombre, total_edificio, total_dormitorio, total_cuarto, total_estudiante
        }
    """
    serializer_class = Rep_Total_by_Sede_Serializer
    queryset = sede.Sede.objects.annotate(
        total_edificios=Count('edificios'),
        total_dormitorios=Count('edificios__dormitorios'),
        total_cuartos=Count('edificios__dormitorios__cuartos'),
        )
    permission_classes = [IsEspecialista]


class Rep_Total(generics.ListAPIView):
    serializer_class = Rep_Total_Serializer
    
    def get(self, request, *args, **kwargs):
        total_sedes = sede.Sede.objects.count()
        total_edificios = edificio.Edificio.objects.count()
        total_dormitorios = dormitorio.Dormitorio.objects.count()
        total_cuartos = cuarto.Cuarto.objects.count()
        total_estudiantes = estudiante.Estudiante.objects.count()

        totals = {
            'total_sedes': total_sedes,
            'total_edificios': total_edificios,
            'total_dormitorios': total_dormitorios,
            'total_cuartos': total_cuartos,
            'total_estudiantes': total_estudiantes,
        }

        serializer = self.get_serializer(totals)
        return Response(serializer.data)
    
    
class Rep_Ocupacion_Total(generics.ListAPIView):
    pass

class Rep_Ocupacion_By_Sede(generics.ListAPIView):
    pass

class Rep_Ocupacion_Edificio(generics.ListAPIView):
    pass

class Rep_Ocupacion_By_Dormitorio(generics.ListAPIView):
    pass

class Rep_Ocupacion_By_Cuarto(generics.ListAPIView):
    pass