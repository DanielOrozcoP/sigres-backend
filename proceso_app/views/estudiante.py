from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from proceso_app.serializers.estudiante import EstudianteSerializers
from proceso_app.models.estudiante import Estudiante
from control_acceso_app.auth.permissions import IsJ_BecaOrIsEspecialista

# Create your views here.


class EstudianteCreateView(generics.CreateAPIView):  # Clase para crear un nuevo estudiante
    serializer_class = EstudianteSerializers  # Define el serializer que se utilizará
    queryset = Estudiante.objects.all()
    permission_classes = [IsJ_BecaOrIsEspecialista]



class EstudianteUpdateView(generics.UpdateAPIView):
    serializer_class = EstudianteSerializers
    queryset = Estudiante.objects.all()
    permission_classes = [IsJ_BecaOrIsEspecialista]



class EstudianteDetailsView(generics.RetrieveAPIView):
    serializer_class = EstudianteSerializers
    queryset = Estudiante.objects.all()
    permission_classes = [IsJ_BecaOrIsEspecialista]



class EstudianteDeleteView(generics.DestroyAPIView):
    serializer_class = EstudianteSerializers
    queryset = Estudiante.objects.all()
    permission_classes = [IsJ_BecaOrIsEspecialista]

class EstudianteListView(generics.ListAPIView):
    serializer_class = EstudianteSerializers
    queryset = Estudiante.objects.all()
    permission_classes = [IsJ_BecaOrIsEspecialista]