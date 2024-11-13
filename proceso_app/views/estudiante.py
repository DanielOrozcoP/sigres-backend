from django.http import Http404#-
from django.shortcuts import get_object_or_404#-
from rest_framework import generics, status#-
from rest_framework.response import Response#-
from proceso_app.serializers.estudiante import EstudianteSerializers#-
from proceso_app.models.estudiante import Estudiante#-
from control_acceso_app.auth.permissions import IsJ_BecaOrIsEspecialista#-
class EstudianteCreateView(generics.CreateAPIView):
    """
    Clase para crear un nuevo estudiante. Utiliza un serializer para validar y crear instancias de Estudiante.
    Hereda de generics.CreateAPIView, que proporciona una vista genérica para crear objetos a través de un serializer.

    Atributos:
    serializer_class: Define el serializer que se utilizará para validar y serializar los datos de entrada.
    queryset: Define el conjunto de objetos Estudiante que se utilizará para realizar operaciones de base de datos.
    permission_classes: Define las clases de permisos que se utilizarán para controlar el acceso a esta vista.
    """
    serializer_class = EstudianteSerializers
    queryset = Estudiante.objects.all()
    permission_classes = [IsJ_BecaOrIsEspecialista]


class EstudianteUpdateView(generics.UpdateAPIView):
    """
    Clase para actualizar un estudiante existente. Utiliza un serializer para validar y actualizar instancias de Estudiante.
    Hereda de generics.UpdateAPIView, que proporciona una vista genérica para actualizar objetos a través de un serializer.

    Atributos:
    serializer_class: Define el serializer que se utilizará para validar y serializar los datos de entrada.
    queryset: Define el conjunto de objetos Estudiante que se utilizará para realizar operaciones de base de datos.
    permission_classes: Define las clases de permisos que se utilizarán para controlar el acceso a esta vista.
    """
    serializer_class = EstudianteSerializers
    queryset = Estudiante.objects.all()
    permission_classes = [IsJ_BecaOrIsEspecialista]


class EstudianteDetailsView(generics.RetrieveAPIView):
    """
    Clase para recuperar detalles de un estudiante específico. Utiliza un serializer para serializar los datos de salida.
    Hereda de generics.RetrieveAPIView, que proporciona una vista genérica para recuperar objetos a través de un serializer.

    Atributos:
    serializer_class: Define el serializer que se utilizará para serializar los datos de salida.
    queryset: Define el conjunto de objetos Estudiante que se utilizará para realizar operaciones de base de datos.
    permission_classes: Define las clases de permisos que se utilizarán para controlar el acceso a esta vista.
    """
    serializer_class = EstudianteSerializers
    queryset = Estudiante.objects.all()
    permission_classes = [IsJ_BecaOrIsEspecialista]


class EstudianteDeleteView(generics.DestroyAPIView):
    """
    Clase para eliminar un estudiante existente.
    Hereda de generics.DestroyAPIView, que proporciona una vista genérica para eliminar objetos.

    Atributos:
    serializer_class: Define el serializer que se utilizará para serializar los datos de salida.
    queryset: Define el conjunto de objetos Estudiante que se utilizará para realizar operaciones de base de datos.
    permission_classes: Define las clases de permisos que se utilizarán para controlar el acceso a esta vista.
    """
    serializer_class = EstudianteSerializers
    queryset = Estudiante.objects.all()
    permission_classes = [IsJ_BecaOrIsEspecialista]


class EstudianteListView(generics.ListAPIView):
    """
    Clase para recuperar una lista de estudiantes. Utiliza un serializer para serializar los datos de salida.
    Hereda de generics.ListAPIView, que proporciona una vista genérica para listar objetos a través de un serializer.

    Atributos:
    serializer_class: Define el serializer que se utilizará para serializar los datos de salida.
    queryset: Define el conjunto de objetos Estudiante que se utilizará para realizar operaciones de base de datos.
    permission_classes: Define las clases de permisos que se utilizarán para controlar el acceso a esta vista.
    """
    serializer_class = EstudianteSerializers
    queryset = Estudiante.objects.all()
    permission_classes = [IsJ_BecaOrIsEspecialista]
