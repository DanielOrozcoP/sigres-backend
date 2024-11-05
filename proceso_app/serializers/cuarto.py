from rest_framework import serializers
from proceso_app.models.cuarto import Cuarto
from proceso_app.serializers.estudiante import EstudianteSerializers


class CuartoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuarto
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request', None)
        if request and 'cuarto/' in request.path:
            # Verifica si 'instance' es un objeto de modelo antes de intentar acceder a sus atributos
            if isinstance(instance, Cuarto):
                estudiantes = self.get_estudiantes(instance)
                representation['estudiantes'] = estudiantes
        return representation

    def get_estudiantes(self, instance):
        estudiantes = instance.estudiantes.all()
        return EstudianteSerializers(estudiantes, many=True, read_only=True).data
