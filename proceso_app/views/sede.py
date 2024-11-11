from django.shortcuts import get_object_or_404
from rest_framework import generics
from proceso_app.models.sede import Sede
from proceso_app.serializers.sede import SedeSerializer
from control_acceso_app.auth.permissions import IsEspecialista


# Create your views here.

class SedeCreateView(generics.CreateAPIView):
    serializer_class = SedeSerializer
    permission_classes = [IsEspecialista]

class SedeUpdateView(generics.UpdateAPIView):
    serializer_class = SedeSerializer
    queryset = Sede.objects.all()
    permission_classes = [IsEspecialista]


class SedeDetailsView(generics.RetrieveAPIView):
    serializer_class = SedeSerializer
    queryset = Sede.objects.all()
    permission_classes = [IsEspecialista]


class SedeDeleteView(generics.DestroyAPIView):
    serializer_class = SedeSerializer
    queryset = Sede.objects.all()
    permission_classes = [IsEspecialista]


class SedeListView(generics.ListAPIView):
    serializer_class = SedeSerializer
    queryset = Sede.objects.all()
    permission_classes = [IsEspecialista]
