from django.shortcuts import get_object_or_404
from rest_framework import generics
from proceso_app.serializers.cuarto import CuartoSerializer
from proceso_app.models.cuarto import Cuarto


# Create your views here.

class CuartoCreateView(generics.CreateAPIView):  # Clase para crear un nuevo estudiante
    serializer_class = CuartoSerializer  # Define el serializer que se utilizará

    def perform_create(self, serializer):  # Método que se llama al crear un nuevo objeto
        serializer = CuartoSerializer(data=self.request.data)
        if serializer.is_valid():
            serializer.save()  # Guarda el nuevo objeto asociado al estudiante encontrado


class CuartoListView(generics.ListAPIView):
    serializer_class = CuartoSerializer

    def get_queryset(self):
        """
        Método que retorna el queryset de objetos a listar.
        Endpoint:{
            - /api/cuarto/list/
            - /api/cuarto/list/?{Parametro de busqueda}={valor}
            }
        Parámetros de búsqueda posibles:{
            'id','codigo'
            'capacidad','ocupacion'
            'dormitorioID'
            }
        Retorna:{
            Un queryset de objetos Cuarto que cumplen con los criterios de búsqueda.
            }
        """
        queryset = Cuarto.objects.all()
        query_params = self.request.query_params
        for key, value in query_params.items():
            queryset = queryset.filter(**{key: value})
        print(f'Queryset: {queryset}')
        return queryset


class CuartoUpdateView(generics.UpdateAPIView):
    serializer_class = CuartoSerializer

    def get_object(self):  # Sobreescribir el metodo get_object()
        queryset = Cuarto.objects.all()  # Consulta
        cuarto = get_object_or_404(queryset, codigo=self.request.query_params.get('codigo'))
        return cuarto


class CuartoDetailsView(generics.RetrieveAPIView):
    serializer_class = CuartoSerializer

    def get_object(self):
        queryset = Cuarto.objects.all()
        cuarto = get_object_or_404(queryset, codigo=self.request.query_params.get('codigo'))
        return cuarto


class CuartoDeleteView(generics.DestroyAPIView):
    serializer_class = CuartoSerializer

    def get_object(self):
        queryset = Cuarto.objects.all()
        cuarto = get_object_or_404(queryset, codigo=self.request.query_params.get('codigo'))
        return cuarto
