from rest_framework import serializers
from proceso_app.serializers.cuarto import CuartoSerializer
from proceso_app.models.dormitorio import Dormitorio


class DormitorioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dormitorio
        fields = "__all__"

