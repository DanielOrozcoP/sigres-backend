from rest_framework import serializers
from proceso_app.models.sede import Sede

class Rep_Total_by_Sede_Serializer(serializers.ModelSerializer):
    total_edificios = serializers.IntegerField(read_only=True)
    total_dormitorios = serializers.IntegerField(read_only=True)
    total_cuartos = serializers.IntegerField(read_only=True)
    total_estudiantes = serializers.IntegerField(read_only=True)

    class Meta:
        model = Sede
        fields = [
            'codigo','nombre','total_edificios', 'total_dormitorios','total_cuartos','total_estudiantes'
        ]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        # Contar edificios
        representation['total_edificios'] = instance.edificios.count()
        
        # Contar dormitorios
        representation['total_dormitorios'] = sum(edificio.dormitorios.count() for edificio in instance.edificios.all())
        
        # Contar cuartos
        representation['total_cuartos'] = sum(
            dormitorio.cuartos.count() for edificio in instance.edificios.all() 
            for dormitorio in edificio.dormitorios.all()
        )
        
        # Contar estudiantes
        representation['total_estudiantes'] = sum(
            cuarto.estudiantes.count() for edificio in instance.edificios.all() 
            for dormitorio in edificio.dormitorios.all() 
            for cuarto in dormitorio.cuartos.all()
        )
        
        return representation
    

class Rep_Total_Serializer(serializers.Serializer):
    total_sedes = serializers.IntegerField()
    total_edificios = serializers.IntegerField()
    total_dormitorios = serializers.IntegerField()
    total_cuartos = serializers.IntegerField()
    total_estudiantes = serializers.IntegerField()