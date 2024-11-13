from django.shortcuts import get_object_or_404#-
from rest_framework import generics#-
from proceso_app.models.edificio import Edificio#-
from proceso_app.serializers.edificio import EdificioSerializer#-
from control_acceso_app.auth.permissions import IsEspecialista#-
from django.db.models import Count
class EdificioCreateView(generics.CreateAPIView):
    """
    This view is responsible for creating new Edificio instances.

    Parameters:
    - serializer_class: The serializer class used to validate and serialize the input data.
    - permission_classes: The list of permission classes that determine if a user has permission to access this view.

    Returns:
    - An HTTP response with the serialized Edificio instance if the request is valid and the user has permission.
    """
    serializer_class = EdificioSerializer
    permission_classes = [IsEspecialista]


class EdificioUpdateView(generics.UpdateAPIView):
    """
    This view is responsible for updating existing Edificio instances.

    Parameters:
    - serializer_class: The serializer class used to validate and serialize the input data.
    - queryset: The queryset of Edificio instances that can be updated.
    - permission_classes: The list of permission classes that determine if a user has permission to access this view.

    Returns:
    - An HTTP response with the serialized updated Edificio instance if the request is valid and the user has permission.
    """
    serializer_class = EdificioSerializer
    queryset = Edificio.objects.all()  # Consulta
    permission_classes = [IsEspecialista]


class EdificioDetailsView(generics.RetrieveAPIView):
    """
    This view is responsible for retrieving a single Edificio instance.

    Parameters:
    - serializer_class: The serializer class used to serialize the Edificio instance.
    - queryset: The queryset of Edificio instances that can be retrieved.
    - permission_classes: The list of permission classes that determine if a user has permission to access this view.

    Returns:
    - An HTTP response with the serialized Edificio instance if the request is valid and the user has permission.
    """
    serializer_class = EdificioSerializer
    queryset = Edificio.objects.annotate(cant_dormitorios=Count("dormitorios"))  # Consulta
    permission_classes = [IsEspecialista]


class EdificioDeleteView(generics.DestroyAPIView):
    """
    This view is responsible for deleting an existing Edificio instance.

    Parameters:
    - serializer_class: The serializer class used to serialize the Edificio instance.
    - queryset: The queryset of Edificio instances that can be deleted.
    - permission_classes: The list of permission classes that determine if a user has permission to access this view.

    Returns:
    - An HTTP response with a status code 204 (No Content) if the request is valid and the user has permission.
    """
    serializer_class = EdificioSerializer
    queryset = Edificio.objects.all()  # Consulta
    permission_classes = [IsEspecialista]


class EdificioListView(generics.ListAPIView):
    """
    This view is responsible for retrieving a list of Edificio instances.

    Parameters:
    - serializer_class: The serializer class used to serialize the Edificio instances.
    - queryset: The queryset of Edificio instances that can be retrieved.
    - permission_classes: The list of permission classes that determine if a user has permission to access this view.

    Returns:
    - An HTTP response with the serialized list of Edificio instances if the request is valid and the user has permission.
    """
    serializer_class = EdificioSerializer
    queryset = Edificio.objects.all()  # Consulta   
    permission_classes = [IsEspecialista]
