from django.contrib import admin
from proceso_app.models import sede,edificio,dormitorio,cuarto,estudiante 

# Register your models here.

admin.site.register(sede.Sede)
admin.site.register(edificio.Edificio)
admin.site.register(dormitorio.Dormitorio)
admin.site.register(cuarto.Cuarto)
admin.site.register(estudiante.Estudiante)
