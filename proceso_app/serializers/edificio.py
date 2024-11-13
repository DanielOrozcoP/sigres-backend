from rest_framework import serializers
from proceso_app.serializers.dormitorio import DormitorioSerializer
from proceso_app.models.edificio import Edificio
#from proceso.sede.api.serializer import SedeSerializer


class EdificioSerializer(serializers.ModelSerializer):
    cant_dormitorios = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Edificio
        fields = ['codigo','sexo','sedeID','cant_dormitorios','dormitorios']

    def get_cant_dormitorios(self, obj):
        return obj.dormitorios.count()