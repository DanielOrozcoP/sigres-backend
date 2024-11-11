from django.urls import path
from servicios_app.views import get_cuarto_free, asignar_cuarto

urlpatterns = [
    path("cuarto-free/", get_cuarto_free, name="cuarto-free"),
    path("asignar-cuarto/", asignar_cuarto, name="asignar-cuarto")
]
