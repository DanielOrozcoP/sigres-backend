from rest_framework import serializers
from proceso_app.serializers.dormitorio import DormitorioSerializer
from proceso_app.models.edificio import Edificio
#from proceso.sede.api.serializer import SedeSerializer


class EdificioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edificio
        fields = "__all__"

