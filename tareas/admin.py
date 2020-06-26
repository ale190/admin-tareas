from django.contrib import admin
from .models import Sector, Estado, Prioridad, GrupoActividad, Actividad, Solicitud

admin.site.register(Sector)
admin.site.register(Estado)
admin.site.register(Prioridad)
admin.site.register(GrupoActividad)
admin.site.register(Actividad)
admin.site.register(Solicitud)
