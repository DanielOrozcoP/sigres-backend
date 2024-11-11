from django.urls import path
from proceso_app.views.sede import SedeCreateView,SedeListView,SedeDetailsView,SedeDeleteView,SedeUpdateView
from proceso_app.views.edificio import EdificioCreateView,EdificioDeleteView,EdificioDetailsView,EdificioListView,EdificioUpdateView
from proceso_app.views.dormitorio import DormitorioCreateView,DormitorioDeleteView,DormitorioDetailsView,DormitorioListView,DormitorioUpdateView
from proceso_app.views.cuarto import CuartoCreateView,CuartoDeleteView,CuartoDetailsView,CuartoListView,CuartoUpdateView
from proceso_app.views.estudiante import EstudianteCreateView,EstudianteDeleteView,EstudianteDetailsView,EstudianteUpdateView,EstudianteListView

urlpatterns = [
    # * Sede
    path("sede/create/", SedeCreateView.as_view(), name="sede-create"),
    path("sede/update/<str:pk>/", SedeUpdateView.as_view(), name="sede-update"),
    path("sede/delete/<str:pk>/", SedeDeleteView.as_view(), name="sede-delete"),
    path("sede/details/<str:pk>/", SedeDetailsView.as_view(), name="sede-details"),
    path("sede/list/", SedeListView.as_view(), name="sede-list"),
    # * Edificio
    path("edificio/create/", EdificioCreateView.as_view(), name="edificio-create"),
    path("edificio/update/<str:pk>/", EdificioUpdateView.as_view(), name="edificio-update"),
    path("edificio/delete/<str:pk>/", EdificioDeleteView.as_view(), name="edificio-delete"),
    path("edificio/details/<str:pk>/", EdificioDetailsView.as_view(), name="edificio-details"),
    path("edificio/list/", EdificioListView.as_view(), name="edificio-list"),
    # * Dormitorio
    path("dormitorio/create/", DormitorioCreateView.as_view(), name="dormitorio-create"),
    path("dormitorio/update/<str:pk>/", DormitorioUpdateView.as_view(), name="dormitorio-update"),
    path("dormitorio/delete/<str:pk>/", DormitorioDeleteView.as_view(), name="dormitorio-delete"),
    path("dormitorio/details/<str:pk>/", DormitorioDetailsView.as_view(), name="dormitorio-details"),
    path("dormitorio/list/", DormitorioListView.as_view(), name="dormitorio-list"),
    # * Cuarto
    path("cuarto/create/", CuartoCreateView.as_view(), name="cuarto-create"),
    path("cuarto/update/<str:pk>/", CuartoUpdateView.as_view(), name="cuarto-update"),
    path("cuarto/delete/<str:pk>/", CuartoDeleteView.as_view(), name="cuarto-delete"),
    path("cuarto/details/<str:pk>/", CuartoDetailsView.as_view(), name="cuarto-details"),
    path("cuarto/list/", CuartoListView.as_view(), name="cuarto-list"),
    # * Estudiante
    path("estudiante/create/", EstudianteCreateView.as_view(), name="estudiante-create"),
    path("estudiante/update/<str:pk>/", EstudianteUpdateView.as_view(), name="estudiante-update"),
    path("estudiante/delete/<str:pk>/", EstudianteDeleteView.as_view(), name="estudiante-delete"),
    path("estudiante/details/<str:pk>/", EstudianteDetailsView.as_view(), name="estudiante-details"),
    path("estudiante/list/", EstudianteListView.as_view(), name="estudiante-list"),
]
