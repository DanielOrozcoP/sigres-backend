from ..serializers.reportes import( 
    Rep_Total_by_Sede_Serializer, 
    Rep_Total_Serializer,
    Rep_Ocupacion_Total_Serializer,
    Rep_Ocupacion_By_Sede_Serializer,
    Rep_Ocupacion_Edificio_Serializer
)
from proceso_app.models import (
    sede, 
    edificio, 
    dormitorio,
    cuarto,
    estudiante
)
from rest_framework.response import Response
from rest_framework import generics
from django.db.models import Count, F, Sum
from control_acceso_app.auth.permissions import IsEspecialista

class Rep_Total_by_Sede(generics.ListAPIView):
    """
    This class represents a view for generating a report of total sedes, edificios, and cuartos.
    It uses Django REST framework's ListAPIView and is restricted to users with the 'IsEspecialista' permission.
    Attributes:
    - serializer_class: The serializer class used to serialize the queryset.
    - permission_classes: The list of permission classes required to access this view.
    Methods:
    - get_queryset: A method that retrieves the queryset for the report. It annotates each sede with the total number of edificios, dormitorios, and cuartos.
    """
    serializer_class = Rep_Total_by_Sede_Serializer
    permission_classes = [IsEspecialista]

    def get_queryset(self):
        """
        Retrieves the queryset for the report.
        Returns:
        - A QuerySet of sedes, annotated with the total number of edificios, dormitorios, and cuartos.
        """
        return (
            sede.Sede.objects.annotate(
                total_edificios=Count('edificios'),
                total_dormitorios=Count('edificios__dormitorios'),
                total_cuartos=Count('edificios__dormitorios__cuartos'),
            )
        )

class Rep_Total(generics.ListAPIView):
    """
    A view for retrieving total counts of various entities in the system.
    This view inherits from Django REST framework's ListAPIView and provides
    a summary of the total number of sedes, edificios, dormitorios, cuartos,
    and estudiantes in the system.
    Attributes:
        serializer_class (Serializer): The serializer class used for data serialization.
    """
    serializer_class = Rep_Total_Serializer

    def get_queryset(self):
        """
        Retrieve the total counts of various entities.
        Returns:
            dict: A dictionary containing the total counts of sedes, edificios,
                dormitorios, cuartos, and estudiantes.
        """
        return {
            'total_sedes': sede.Sede.objects.count(),
            'total_edificios': edificio.Edificio.objects.count(),
            'total_dormitorios': dormitorio.Dormitorio.objects.count(),
            'total_cuartos': cuarto.Cuarto.objects.count(),
            'total_estudiantes': estudiante.Estudiante.objects.count(),
        }

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to retrieve and serialize total counts.
        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        Returns:
            Response: A serialized representation of the total counts.
        """
        totals = self.get_queryset()
        serializer = self.get_serializer(totals)
        return Response(serializer.data)


class Rep_Ocupacion_Total(generics.ListAPIView):
    """
    A view for retrieving the total occupancy report for all rooms.
    This class inherits from Django REST framework's ListAPIView and provides
    an endpoint to get aggregated data about room capacities and occupancies.
    Attributes:
        serializer_class (Serializer): The serializer class used for data serialization.
    """
    serializer_class = Rep_Ocupacion_Total_Serializer

    def get(self, request, *args, **kwargs):
        """
        Retrieve and return the total occupancy report.
        This method calculates the total capacity, available space, and current
        occupancy across all rooms.
        Returns:
            Response: A serialized representation of the total occupancy data,
                    including total capacity, total available space, and
                    total current occupancy.
        """
        totals = cuarto.Cuarto.objects.aggregate(
            total_capacidad=Sum('capacidad'),
            total_disponible=Sum(F('capacidad') - F('ocupacion')),
            total_ocupacion=Sum('ocupacion')
        )
        totals = {key: value or 0 for key, value in totals.items()}
        serializer = self.get_serializer(totals)
        return Response(serializer.data)


class Rep_Ocupacion_By_Sede(generics.ListAPIView):
    """
    A view for retrieving occupancy reports for each sede (campus).
    This class provides an API endpoint that returns occupancy statistics
    for each sede, including total capacity, current occupancy, and
    available space.
    """
    serializer_class = Rep_Ocupacion_By_Sede_Serializer

    def get_queryset(self):
        """
        Retrieves and processes the queryset for sede occupancy reports.
        This method aggregates data from related models (edificios, dormitorios, cuartos)
        to calculate occupancy statistics for each sede.
        Returns:
            QuerySet: A queryset of sede objects annotated with occupancy statistics.
                    Each object contains the following fields:
                    - codigo: The unique identifier of the sede
                    - total_capacidad: The total capacity of all cuartos in the sede
                    - total_ocupacion: The current total occupancy of all cuartos in the sede
                    - total_disponibilidad: The total available space in the sede
        Note:
            Only sedes with available space (total_disponibilidad > 0) are included in the result.
        """
        return (
            sede.Sede.objects.annotate(
                total_capacidad=Sum('edificios__dormitorios__cuartos__capacidad'),
                total_ocupacion=Sum('edificios__dormitorios__cuartos__ocupacion'),
                total_disponibilidad=Sum(
                    F('edificios__dormitorios__cuartos__capacidad') - F('edificios__dormitorios__cuartos__ocupacion')
                )
            )
            .filter(total_disponibilidad__gt=0)
            .values('codigo', 'total_capacidad', 'total_ocupacion', 'total_disponibilidad')
        )


class Rep_Ocupacion_Edificio(generics.ListAPIView):
    """
    A view for retrieving occupancy reports for each edificio (building).
    This class provides an API endpoint that returns occupancy statistics
    for each edificio, including total capacity, current occupancy, and
    available space.
    """
    serializer_class = Rep_Ocupacion_Edificio_Serializer

    def get_queryset(self):
        """
        Retrieves and processes the queryset for edificio occupancy reports.
        This method aggregates data from related models (dormitorios, cuartos)
        to calculate occupancy statistics for each edificio.
        Returns:
            QuerySet: A queryset of edificio objects annotated with occupancy statistics.
                    Each object contains the following fields:
                    - codigo: The unique identifier of the edificio
                    - total_capacidad: The total capacity of all cuartos in the edificio
                    - total_ocupacion: The current total occupancy of all cuartos in the edificio
                    - total_disponibilidad: The total available space in the edificio

        Note:
            Only edificios with available space (total_disponibilidad > 0) are included in the result.
        """
        return (
            edificio.Edificio.objects.annotate(
                total_capacidad=Sum('dormitorios__cuartos__capacidad'),
                total_ocupacion=Sum('dormitorios__cuartos__ocupacion'),
                total_disponibilidad=Sum(
                    F('dormitorios__cuartos__capacidad') - F('dormitorios__cuartos__ocupacion')
                )
            )
            .filter(total_disponibilidad__gt=0)
            .values('codigo', 'total_capacidad', 'total_ocupacion', 'total_disponibilidad')
        )


class Rep_Ocupacion_By_Dormitorio(generics.ListAPIView):
    pass

class Rep_Ocupacion_By_Cuarto(generics.ListAPIView):
    pass