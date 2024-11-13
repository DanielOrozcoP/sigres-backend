from rest_framework import generics#-
from proceso_app.serializers.dormitorio import DormitorioSerializer#-
from proceso_app.models.dormitorio import Dormitorio#-
from control_acceso_app.auth.permissions import IsEspecialista#-
class DormitorioListView(generics.ListAPIView):
    """
    This class provides a list of all Dormitorios.

    Attributes:
    serializer_class: The serializer class used to serialize the Dormitorio instances.
    queryset: The queryset of Dormitorio instances to be listed.
    permission_classes: The permissions required to access this view.
    """
    serializer_class = DormitorioSerializer
    queryset = Dormitorio.objects.all()
    permission_classes = [IsEspecialista]


class DormitorioCreateView(generics.CreateAPIView):
    """
    This class provides a view to create a new Dormitorio instance.

    Attributes:
    serializer_class: The serializer class used to serialize the Dormitorio instance.
    permission_classes: The permissions required to access this view.
    """
    serializer_class = DormitorioSerializer
    permission_classes = [IsEspecialista]


class DormitorioUpdateView(generics.UpdateAPIView):
    """
    This class provides a view to update an existing Dormitorio instance.

    Attributes:
    serializer_class: The serializer class used to serialize the Dormitorio instance.
    queryset: The queryset of Dormitorio instances to be updated.
    permission_classes: The permissions required to access this view.
    """
    serializer_class = DormitorioSerializer
    queryset = Dormitorio.objects.all()
    permission_classes = [IsEspecialista]


class DormitorioDeleteView(generics.DestroyAPIView):
    """
    This class provides a view to delete an existing Dormitorio instance.

    Attributes:
    serializer_class: The serializer class used to serialize the Dormitorio instance.
    queryset: The queryset of Dormitorio instances to be deleted.
    permission_classes: The permissions required to access this view.
    """
    serializer_class = DormitorioSerializer
    queryset = Dormitorio.objects.all()
    permission_classes = [IsEspecialista]


class DormitorioDetailsView(generics.RetrieveAPIView):
    """
    This class provides a view to retrieve details of a specific Dormitorio instance.

    Attributes:
    serializer_class: The serializer class used to serialize the Dormitorio instance.
    queryset: The queryset of Dormitorio instances to be retrieved.
    permission_classes: The permissions required to access this view.
    """
    serializer_class = DormitorioSerializer
    queryset = Dormitorio.objects.all()
    permission_classes = [IsEspecialista]

