from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from proceso_app.serializers.estudiante import EstudianteSerializers
from proceso_app.models.estudiante import Estudiante


# Create your views here.


class EstudianteCreateView(generics.CreateAPIView):  # Clase para crear un nuevo estudiante
    serializer_class = EstudianteSerializers  # Define el serializer que se utilizará

    def perform_create(self, serializer):  # Método que se llama al crear un nuevo objeto
        # pk = self.kwargs['pk']  # Obtiene el ID (clave primaria) del estudiante desde los argumentos de la URL
        # estudiante = Estudiante.objects.get(pk=pk)  # Busca el estudiante en la base de datos usando la clave primaria
        serializer = EstudianteSerializers(data=self.request.data)
        if serializer.is_valid():
            serializer.save()  # Guarda el nuevo objeto asociado al estudiante encontrado


class EstudiantesListView(generics.ListAPIView):
    serializer_class = EstudianteSerializers
    def get_queryset(self):
        """
        Método que retorna el queryset de objetos a listar.
        Endpoint:{
            - /api/estudiante/list/
            - /api/estudiante/list/?{Parametro de busqueda}={valor}
            }
        Parámetros de búsqueda posibles:{
            'id','carnet_identidad'
            'nombre','apellido'
            'facultad','carrera'
            'ano_academico','eliminado'
            }
        Retorna:{
            Un queryset de objetos Estudiante que cumplen con los criterios de búsqueda.
            }
        """
        queryset = Estudiante.objects.filter(eliminado=False)
        query_params = self.request.query_params
        for key, value in query_params.items():
            queryset = queryset.filter(**{key: value})
        print(f'Queryset: {queryset}')
        return queryset


class EstudianteUpdateView(generics.UpdateAPIView):
    serializer_class = EstudianteSerializers

    def get_object(self):  # Sobreescribir el metodo get_object()
        queryset = Estudiante.objects.filter(eliminado=False)  # Consulta
        estudiante = get_object_or_404(queryset, carnet_identidad=self.request.query_params.get('carnet_identidad'))
        return estudiante


class EstudianteDetailsView(generics.RetrieveAPIView):
    serializer_class = EstudianteSerializers

    def get_object(self):
        queryset = Estudiante.objects.filter(eliminado=False)
        estudiante = get_object_or_404(queryset, carnet_identidad=self.request.query_params.get('carnet_identidad'))
        return estudiante


class EstudianteDeleteView(generics.DestroyAPIView):
    serializer_class = EstudianteSerializers

    def get_object(self):
        queryset = Estudiante.objects.filter(eliminado=False)
        estudiante = get_object_or_404(queryset, carnet_identidad=self.request.query_params.get('carnet_identidad'))
        return estudiante
