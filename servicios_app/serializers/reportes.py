from rest_framework import serializers
from proceso_app.models import (
    sede, 
    edificio, 
    dormitorio,
    cuarto,
    estudiante
)

class Rep_Total_by_Sede_Serializer(serializers.ModelSerializer):
    total_edificios = serializers.IntegerField(read_only=True)
    total_dormitorios = serializers.IntegerField(read_only=True)
    total_cuartos = serializers.IntegerField(read_only=True)
    total_estudiantes = serializers.IntegerField(read_only=True)

    class Meta:
        model = sede.Sede
        fields = [
            'codigo','nombre','total_edificios', 'total_dormitorios','total_cuartos','total_estudiantes'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['total_edificios'] = instance.edificios.count()
        representation['total_dormitorios'] = sum(edificio.dormitorios.count() for edificio in instance.edificios.all())
        representation['total_cuartos'] = sum(
            dormitorio.cuartos.count() for edificio in instance.edificios.all() 
            for dormitorio in edificio.dormitorios.all()
        )
        representation['total_estudiantes'] = sum(
            cuarto.estudiantes.count() for edificio in instance.edificios.all() 
            for dormitorio in edificio.dormitorios.all() 
            for cuarto in dormitorio.cuartos.all()
        ) 
        return representation
    

class Rep_Total_Serializer(serializers.Serializer):
    total_sedes = serializers.IntegerField(read_only=True, help_text="Total de sedes.")
    total_edificios = serializers.IntegerField(read_only=True, help_text="Total de edificios.")
    total_dormitorios = serializers.IntegerField(read_only=True, help_text="Total de dormitorios.")
    total_cuartos = serializers.IntegerField(read_only=True, help_text="Total de cuartos.")
    total_estudiantes = serializers.IntegerField(read_only=True, help_text="Total de estudiantes.")

class Rep_Ocupacion_Total_Serializer(serializers.Serializer):
    total_capacidad = serializers.IntegerField(read_only=True)
    total_disponible = serializers.IntegerField(read_only=True)
    total_ocupacion = serializers.IntegerField(read_only=True)

class Rep_Ocupacion_By_Sede_Serializer(serializers.ModelSerializer):
    """
    Serializador para representar la ocupación y capacidad de los edificios.
    """
    total_capacidad = serializers.IntegerField(read_only=True, help_text='Capacidad total de los cuartos en el edificio.')
    total_ocupacion = serializers.IntegerField(read_only=True, help_text='Ocupación total de los cuartos en el edificio.')
    total_disponibilidad = serializers.IntegerField(read_only=True, help_text='Disponibilidad total de cuartos en el edificio.')

    class Meta:
        model = sede.Sede  # Asegúrate de que este sea el modelo correcto
        fields = ['codigo', 'total_capacidad', 'total_ocupacion', 'total_disponibilidad']

class Rep_Ocupacion_Edificio_Serializer(serializers.ModelSerializer):
    """
    Serializador para representar la ocupación y capacidad de los edificios.
    """
    total_capacidad = serializers.IntegerField(read_only=True, help_text='Capacidad total de los cuartos en el edificio.')
    total_ocupacion = serializers.IntegerField(read_only=True, help_text='Ocupación total de los cuartos en el edificio.')
    total_disponibilidad = serializers.IntegerField(read_only=True, help_text='Disponibilidad total de cuartos en el edificio.')

    class Meta:
        model = edificio.Edificio  # Asegúrate de que este sea el modelo correcto
        fields = ['codigo', 'total_capacidad', 'total_ocupacion', 'total_disponibilidad']
