from django.urls import path
from proceso_app.views.sede import SedeCreateView,SedeListView,SedeDetailsView,SedeDeleteView,SedeUpdateView

urlpatterns = [
    # * Sede
    path("sede/create/", SedeCreateView.as_view(), name="sede-create"),
    path("sede/update/<str:pk>/", SedeUpdateView.as_view(), name="sede-update"),
    path("sede/delete/<str:pk>/", SedeDeleteView.as_view(), name="sede-delete"),
    path("sede/details/<str:pk>/", SedeDetailsView.as_view(), name="sede-details"),
    path("sede/list/", SedeListView.as_view(), name="sede-list"),
    # # * Edificio
    # path("edificio/create/", SedeCreateView.as_view(), name="edificio-create"),
    # path("edificio/update/", SedeUpdateView.as_view(), name="edificio-update"),
    # path("edificio/delete/", SedeDeleteView.as_view(), name="edificio-delete"),
    # path("edificio/details/", SedeDetailsView.as_view(), name="edificio-details"),
    # path("edificio/list/", SedeListView.as_view(), name="edificio-list"),
    # # * Dormitorio
    # path("dormitorio/create/", SedeCreateView.as_view(), name="dormitorio-create"),
    # path("dormitorio/update/", SedeUpdateView.as_view(), name="dormitorio-update"),
    # path("dormitorio/delete/", SedeDeleteView.as_view(), name="dormitorio-delete"),
    # path("dormitorio/details/", SedeDetailsView.as_view(), name="dormitorio-details"),
    # path("dormitorio/list/", SedeListView.as_view(), name="dormitorio-list"),
    # # * Cuarto
    # path("cuarto/create/", SedeCreateView.as_view(), name="cuarto-create"),
    # path("cuarto/update/", SedeUpdateView.as_view(), name="cuarto-update"),
    # path("cuarto/delete/", SedeDeleteView.as_view(), name="cuarto-delete"),
    # path("cuarto/details/", SedeDetailsView.as_view(), name="cuarto-details"),
    # path("cuarto/list/", SedeListView.as_view(), name="cuarto-list"),
    # # * Estudiante
    # path("estudiante/create/", SedeCreateView.as_view(), name="estudiante-create"),
    # path("estudiante/update/", SedeUpdateView.as_view(), name="estudiante-update"),
    # path("estudiante/delete/", SedeDeleteView.as_view(), name="estudiante-delete"),
    # path("estudiante/details/", SedeDetailsView.as_view(), name="estudiante-details"),
    # path("estudiante/list/", SedeListView.as_view(), name="estudiante-list"),
]
