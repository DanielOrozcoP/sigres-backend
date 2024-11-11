from django.shortcuts import get_object_or_404
from rest_framework import generics
from proceso_app.serializers.cuarto import CuartoSerializer
from proceso_app.models.cuarto import Cuarto
from control_acceso_app.auth.permissions import IsEspecialista


# Create your views here.

class CuartoCreateView(generics.CreateAPIView):  # Clase para crear un nuevo estudiante
    serializer_class = CuartoSerializer  # Define el serializer que se utilizará
    permission_classes = [IsEspecialista]

class CuartoListView(generics.ListAPIView):
    serializer_class = CuartoSerializer
    queryset = Cuarto.objects.all()
    permission_classes = [IsEspecialista]


class CuartoUpdateView(generics.UpdateAPIView):
    serializer_class = CuartoSerializer
    queryset = Cuarto.objects.all()
    permission_classes = [IsEspecialista]

class CuartoDetailsView(generics.RetrieveAPIView):
    serializer_class = CuartoSerializer
    queryset = Cuarto.objects.all()
    permission_classes = [IsEspecialista]


class CuartoDeleteView(generics.DestroyAPIView):
    serializer_class = CuartoSerializer
    queryset = Cuarto.objects.all()
    permission_classes = [IsEspecialista]
