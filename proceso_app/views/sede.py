from django.shortcuts import get_object_or_404
from rest_framework import generics
from proceso_app.models.sede import Sede
from proceso_app.models.edificio import Edificio
from proceso_app.serializers.sede import SedeSerializer
from control_acceso_app.auth.permissions import IsEspecialista
from django.db.models import Count
class SedeCreateView(generics.CreateAPIView):
    """
    This view is responsible for creating a new Sede object.

    Parameters:
    - serializer_class: The serializer class used to validate and serialize the input data.
    - permission_classes: The list of permission classes required to access this view.

    Returns:
    - An HTTP response with the serialized Sede object if the request is valid and authorized.
    """
    serializer_class = SedeSerializer
    permission_classes = [IsEspecialista]


class SedeUpdateView(generics.UpdateAPIView):
    """
    This view is responsible for updating an existing Sede object.

    Parameters:
    - serializer_class: The serializer class used to validate and serialize the input data.
    - queryset: The queryset of Sede objects that can be updated.
    - permission_classes: The list of permission classes required to access this view.

    Returns:
    - An HTTP response with the serialized updated Sede object if the request is valid and authorized.
    """
    serializer_class = SedeSerializer
    queryset = Sede.objects.all()
    permission_classes = [IsEspecialista]


class SedeDetailsView(generics.RetrieveAPIView):
    """
    This view is responsible for retrieving a specific Sede object.

    Parameters:
    - serializer_class: The serializer class used to serialize the Sede object.
    - queryset: The queryset of Sede objects that can be retrieved.
    - permission_classes: The list of permission classes required to access this view.

    Returns:
    - An HTTP response with the serialized Sede object if the request is valid and authorized.
    """
    serializer_class = SedeSerializer
    queryset = Sede.objects.annotate(
        total_edificios=Count('edificios'),
        total_dormitorios=Count('edificios__dormitorios'),
        total_cuartos=Count('edificios__dormitorios__cuartos'),
        )
    permission_classes = [IsEspecialista]


class SedeDeleteView(generics.DestroyAPIView):
    """
    This view is responsible for deleting a specific Sede object.

    Parameters:
    - serializer_class: The serializer class used to serialize the Sede object.
    - queryset: The queryset of Sede objects that can be deleted.
    - permission_classes: The list of permission classes required to access this view.

    Returns:
    - An HTTP response with a success message if the Sede object is successfully deleted and the request is valid and authorized.
    """
    serializer_class = SedeSerializer
    queryset = Sede.objects.all()
    permission_classes = [IsEspecialista]


class SedeListView(generics.ListAPIView):
    """
    This view is responsible for retrieving a list of Sede objects.

    Parameters:
    - serializer_class: The serializer class used to serialize the Sede objects.
    - queryset: The queryset of Sede objects that can be listed.
    - permission_classes: The list of permission classes required to access this view.

    Returns:
    - An HTTP response with a list of serialized Sede objects if the request is valid and authorized.
    """
    serializer_class = SedeSerializer
    queryset = Sede.objects.all()
    permission_classes = [IsEspecialista]

