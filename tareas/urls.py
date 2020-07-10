#from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login),
    path('logout', views.logout),
    path('agregarActividad', views.agregarActividad),
    path('agregarActGrupoAct/<int:idGrupoActividad>', views.agregarActGrupoAct),
    path('agregarSolicitud/<int:idActividad>', views.agregarSolicitud),
    path('actividadesFinalizadas', views.actividadesFinalizadas),
    path('finalizarTarea/<int:idActividad>', views.finalizarTarea),
    path('agregarGrupoAct', views.agregarGrupoAct),
    path('editarActividad/<int:idActividad>', views.editarActividad),
    path('welcome', views.welcome),
    path('eliminarActividad/<int:idActividad>', views.eliminarActividad),
    path('editarSolicitud/<int:idSolicitud>', views.editarSolicitud),
    path('listarGrupoAct/<int:idGrupoActividad>', views.listarGrupoAct),
    path('editarGrupoActividad/<int:idGrupoActividad>', views.editarGrupoActividad),
    path('editarGrupoActividadFinalizadas/<int:idGrupoActividad>', views.editarGrupoActividadFinalizadas),
    path('eliminarSolicitud/<int:idSolicitud>', views.eliminarSolicitud),
    path('eliminarGrupoActividad/<int:idGrupoActividad>', views.eliminarGrupoActividad),
]
