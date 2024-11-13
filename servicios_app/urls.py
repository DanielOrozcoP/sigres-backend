from django.urls import path
from servicios_app.views.views import get_cuarto_free, asignar_cuarto
from servicios_app.views.reportes import Rep_Total_by_Sede,Rep_Total

urlpatterns = [
    path("cuarto-free/", get_cuarto_free, name="cuarto-free"),
    path("asignar-cuarto/", asignar_cuarto, name="asignar-cuarto"),
    path("reporte/total-by-sede/", Rep_Total_by_Sede.as_view(), name="rep-total-by-sede"),
    path("reporte/total/", Rep_Total.as_view(), name="rep-total")
]
