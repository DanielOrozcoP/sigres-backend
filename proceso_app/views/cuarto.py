from django.shortcuts import get_object_or_404
from rest_framework import generics
from proceso_app.serializers.cuarto import CuartoSerializer
from proceso_app.models.cuarto import Cuarto
from control_acceso_app.auth.permissions import IsEspecialista


# Create your views here.

class CuartoCreateView(generics.CreateAPIView):
    """
    Clase para crear un nuevo cuarto.

    Utiliza el serializer `CuartoSerializer` para validar y serializar los datos de entrada.
    Requiere permisos de especialista para acceder a esta vista.
    """
    serializer_class = CuartoSerializer  # Define el serializer que se utilizará
    permission_classes = [IsEspecialista]


class CuartoListView(generics.ListAPIView):
    """
    Vista para listar todos los cuartos.

    Utiliza el serializer `CuartoSerializer` para serializar los objetos `Cuarto`.
    Requiere permisos de especialista para acceder a esta vista.
    """
    serializer_class = CuartoSerializer
    queryset = Cuarto.objects.all()
    permission_classes = [IsEspecialista]


class CuartoUpdateView(generics.UpdateAPIView):
    """
    Vista para actualizar un cuarto existente.

    Utiliza el serializer `CuartoSerializer` para validar y serializar los datos de entrada.
    Requiere permisos de especialista para acceder a esta vista.
    """
    serializer_class = CuartoSerializer
    queryset = Cuarto.objects.all()
    permission_classes = [IsEspecialista]


class CuartoDetailsView(generics.RetrieveAPIView):
    """
    Vista para obtener detalles de un cuarto específico.

    Utiliza el serializer `CuartoSerializer` para serializar los objetos `Cuarto`.
    Requiere permisos de especialista para acceder a esta vista.
    """
    serializer_class = CuartoSerializer
    queryset = Cuarto.objects.all()
    permission_classes = [IsEspecialista]


class CuartoDeleteView(generics.DestroyAPIView):
    """
    Vista para eliminar un cuarto existente.

    Utiliza el serializer `CuartoSerializer` para serializar los objetos `Cuarto`.
    Requiere permisos de especialista para acceder a esta vista.
    """
    serializer_class = CuartoSerializer
    queryset = Cuarto.objects.all()
    permission_classes = [IsEspecialista]

