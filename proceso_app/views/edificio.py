from django.shortcuts import get_object_or_404
from rest_framework import generics
from proceso_app.models.edificio import Edificio
from proceso_app.serializers.edificio import EdificioSerializer


# Create your views here.

class EdificioCreateView(generics.CreateAPIView):
    serializer_class = EdificioSerializer

    def perform_create(self, serializer):
        serializer.save()


class EdificioUpdateView(generics.UpdateAPIView):
    serializer_class = EdificioSerializer

    def get_object(self):  # Sobreescribir el metodo get_object()
        queryset = Edificio.objects.all()  # Consulta
        edificio = get_object_or_404(queryset, id=self.request.query_params.get('id'))
        return edificio


class EdificioDetailsView(generics.RetrieveAPIView):
    serializer_class = EdificioSerializer

    def get_object(self):
        queryset = Edificio.objects.all()
        edificio = get_object_or_404(queryset, id=self.request.query_params.get('id'))
        return edificio


class EdificioDeleteView(generics.DestroyAPIView):
    serializer_class = EdificioSerializer

    def get_object(self):
        queryset = Edificio.objects.all()
        edificio = get_object_or_404(queryset, id=self.request.query_params.get('id'))
        return edificio


class EdificioListView(generics.ListAPIView):
    serializer_class = EdificioSerializer

    def get_queryset(self):
        edificio = Edificio.objects.all()
        return edificio