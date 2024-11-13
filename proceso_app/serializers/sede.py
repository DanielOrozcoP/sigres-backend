from rest_framework import serializers
from proceso_app.serializers.edificio import EdificioSerializer
from proceso_app.models.sede import Sede


class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = '__all__'
