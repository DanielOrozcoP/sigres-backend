from rest_framework import serializers
from proceso_app.models.cuarto import Cuarto
from proceso_app.models.estudiante import Estudiante


class EstudianteSerializers(serializers.ModelSerializer):
    cuarto = serializers.SlugRelatedField(
        slug_field='codigo',
        queryset=Cuarto.objects.all()
    )

    class Meta:
        model = Estudiante
        fields = '__all__'
