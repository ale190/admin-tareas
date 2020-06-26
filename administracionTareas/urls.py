"""administracionTareas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('tareas/', include('tareas.urls')),
    path('admin/', admin.site.urls, name="admin"),
    path('login', views.login),
    path('logout', views.logout),
    path('agregarActividad', views.agregarActividad),
    path('agregarActGrupoAct/<int:idGrupoActividad>', views.agregarActGrupoAct),
    path('agregarSolicitud/<int:idActividad>', views.agregarSolicitud),
    path('actividadesFinalizadas', views.actividadesFinalizadas),
    path('finalizarTarea/<int:idActividad>', views.finalizarTarea),
    path('agregarGrupoAct', views.agregarGrupoAct),
    path('editarActividad/<int:idActividad>', views.editarActividad),
    path('', views.welcome),
]