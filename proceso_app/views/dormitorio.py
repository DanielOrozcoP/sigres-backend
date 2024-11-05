from rest_framework import generics
from proceso_app.serializers.dormitorio import DormitorioSerializer
from proceso_app.models.dormitorio import Dormitorio


# Create your views here.

class DormitorioListView(generics.ListAPIView):
    serializer_class = DormitorioSerializer

    def get_queryset(self):
        dormitorio = Dormitorio.objects.all()
        return dormitorio
