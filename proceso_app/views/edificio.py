from django.shortcuts import get_object_or_404
from rest_framework import generics
from proceso_app.models.edificio import Edificio
from proceso_app.serializers.edificio import EdificioSerializer
from control_acceso_app.auth.permissions import IsEspecialista


# Create your views here.

class EdificioCreateView(generics.CreateAPIView):
    serializer_class = EdificioSerializer
    permission_classes = [IsEspecialista]

class EdificioUpdateView(generics.UpdateAPIView):
    serializer_class = EdificioSerializer
    queryset = Edificio.objects.all()  # Consulta
    permission_classes = [IsEspecialista]

class EdificioDetailsView(generics.RetrieveAPIView):
    serializer_class = EdificioSerializer
    queryset = Edificio.objects.all()  # Consulta
    permission_classes = [IsEspecialista]

class EdificioDeleteView(generics.DestroyAPIView):
    serializer_class = EdificioSerializer
    queryset = Edificio.objects.all()  # Consulta
    permission_classes = [IsEspecialista]

class EdificioListView(generics.ListAPIView):
    serializer_class = EdificioSerializer
    queryset = Edificio.objects.all()  # Consulta   
    permission_classes = [IsEspecialista]