from rest_framework import generics
from proceso_app.serializers.dormitorio import DormitorioSerializer
from proceso_app.models.dormitorio import Dormitorio
from control_acceso_app.auth.permissions import IsEspecialista


# Create your views here.

class DormitorioListView(generics.ListAPIView):
    serializer_class = DormitorioSerializer
    queryset = Dormitorio.objects.all()
    permission_classes = [IsEspecialista]

class DormitorioCreateView(generics.CreateAPIView):
    serializer_class = DormitorioSerializer
    permission_classes = [IsEspecialista]


class DormitorioUpdateView(generics.UpdateAPIView):
    serializer_class = DormitorioSerializer
    queryset = Dormitorio.objects.all()
    permission_classes = [IsEspecialista]

class DormitorioDeleteView(generics.DestroyAPIView):
    serializer_class = DormitorioSerializer
    queryset = Dormitorio.objects.all()
    permission_classes = [IsEspecialista]

class DormitorioDetailsView(generics.RetrieveAPIView):
    serializer_class = DormitorioSerializer
    queryset = Dormitorio.objects.all()
    permission_classes = [IsEspecialista]
