#from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from tareas.models import Actividad, Solicitud, Prioridad, GrupoActividad
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.models import User
from . forms import ActividadForm, ActividadFormEdicion, ActividadGrupoForm, SolicitudForm, SolicitudFormEdicion, GrupoActividadForm
import time


# def hello_world(request):
# #return HttpResponse('Hola Mundo')
# saludoInicial = 'Bienvenido'
# context = {'saludoInicial':saludoInicial}
# return render(request, 'home.html', context)


def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/tareas/welcome')

    # Si llegamos al final renderizamos el formulario
    return render(request, "tareas/login.html", {'form': form})

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/tareas/')

def welcome(request, *args, **kwargs):
    #Obtenemos el id del usuario logueado
    idU = User.objects.get(id=request.user.id)
    idUs = idU.id
    #Obtenemos las actividades del usuario logueado y sin informes vinculados
    actividades = Actividad.objects.filter(user=idUs, grupoactividad=None).order_by('prioridad')
    #Obtenemos las actividades del usuario logueado y con informes vinculados
    actividades2 = Actividad.objects.filter(user=idUs).exclude(grupoactividad=None)
    #Obtenemos todas las solicitudes
    solicitudes = Solicitud.objects.all()
    #Obtenemos todas las prioridades
    prioridades = Prioridad.objects.all()
    #Incluimos los resultados en un contexto
    context = {'actividades':actividades,'actividades2':actividades2, 'solicitudes':solicitudes, 'prioridades':prioridades}
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, 'tareas/welcome.html', context)
    # En otro caso redireccionamos al login
    return render(request, "tareas/login.html")

def agregarActividad(request, *args, **kwargs):
    form = ActividadForm()
    context = {'form':form}
    idU = User.objects.get(id=request.user.id)
    idUs = idU.id
    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            comentarios = form.cleaned_data.get('comentarios')
            prioridad = form.cleaned_data.get('prioridad')
            estado = 1
            usuario = idUs
            grupoactividad = form.cleaned_data.get('grupoactividad')
            nuevaTarea = Actividad.objects.create(nombre=nombre,comentarios=comentarios,prioridad=prioridad,estado_id=estado,user_id=usuario,grupoactividad=grupoactividad)
            nuevaTarea.save()
            #mensaje = 'Actividad creada correctamente!'
            context = {'form':form}
            return redirect('/tareas/welcome')
    return render(request, 'tareas/agregarActividad.html', context)

def agregarSolicitud(request, idActividad):
    form = SolicitudForm()
    context = {'form':form}
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            actividad = idActividad
            sector = form.cleaned_data.get('sector')
            estado = 1
            nuevaSolicitud = Solicitud.objects.create(nombre=nombre,actividad_id=actividad,sector=sector,estado_id=estado)
            nuevaSolicitud.save()
            #mensaje = 'Solicitud creada correctamente!'
            context = {'form':form}
            return redirect('/tareas/welcome')
    return render(request, 'tareas/agregarSolicitud.html', context)

def agregarActGrupoAct(request, idGrupoActividad, *args, **kwargs):
    form = ActividadGrupoForm()
    context = {'form':form}
    idU = User.objects.get(id=request.user.id)
    idUs = idU.id
    if request.method == 'POST':
        form = ActividadGrupoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            comentarios = form.cleaned_data.get('comentarios')
            prioridad = form.cleaned_data.get('prioridad')
            estado = 1
            usuario = idUs
            grupoactividad = idGrupoActividad
            nuevaTarea = Actividad.objects.create(nombre=nombre,comentarios=comentarios,prioridad=prioridad,estado_id=estado,user_id=usuario,grupoactividad_id=grupoactividad)
            nuevaTarea.save()
            context = {'form':form}
            return redirect('/tareas/welcome')
    return render(request, 'tareas/agregarActGrupoAct.html', context)

def actividadesFinalizadas(request, *args, **kwargs):
    #Obtenemos el id del usuario logueado
    idU = User.objects.get(id=request.user.id)
    idUs = idU.id
    #Obtenemos las actividades relacionadas al usuario logueado y sin informes
    actividades = Actividad.objects.filter(user=idUs, grupoactividad=None).order_by('prioridad')
    #Obtenemos las actividades relacionadas al usuario logueado y con informes
    actividades2 = Actividad.objects.filter(user=idUs).exclude(grupoactividad=None)
    #Obtenemos todas las solicitudes
    solicitudes = Solicitud.objects.all()
    #Obtenemos todas las prioridades
    prioridades = Prioridad.objects.all()
    #Incluimos los resultados en un contexto
    context = {'actividades':actividades,'actividades2':actividades2,'solicitudes':solicitudes, 'prioridades':prioridades}
    return render(request, "tareas/actividadesFinalizadas.html", context)


def finalizarTarea(request, idActividad):
    fechaF = time.strftime("%Y-%m-%d %H:%M:%S")
    instancia = Actividad.objects.filter(id=idActividad).update(estado_id=2,fechaF=fechaF)
    return redirect('/tareas/actividadesFinalizadas')

def agregarGrupoAct(request):
    form = GrupoActividadForm()
    context = {'form':form}
    if request.method == 'POST':
        form = GrupoActividadForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            prioridad = form.cleaned_data.get('prioridad')
            nuevoGrupoActividad = GrupoActividad.objects.create(nombre=nombre,prioridad=prioridad)
            nuevoGrupoActividad.save()
            #mensaje = 'Solicitud creada correctamente!'
            context = {'form':form}
            return redirect('/tareas/welcome')
    return render(request, 'tareas/agregarGrupoAct.html', context)

def editarActividad(request, idActividad):
    instancia = Actividad.objects.get(id=idActividad)
    solicitudes = Solicitud.objects.filter(actividad_id=idActividad)
    form = ActividadFormEdicion(instance=instancia)
    context = {'form':form,'solicitudes':solicitudes,'instancia':instancia}
    if request.method == "POST":
        form = ActividadFormEdicion(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            #mensaje= "La actividad se modificó correctamente!"
            context = {'form':form,'solicitudes':solicitudes}
            return redirect('/tareas/welcome')
    return render(request, 'tareas/editarActividad.html', context)

def deleteSubTask(request, idSubTask):
    instancia = Subtarea.objects.get(id_sub=idSubTask)
    instancia.delete()
    return render(request, 'tareas/subTarea/subTasks.html')

def eliminarActividad(request, idActividad):
    instancia = Actividad.objects.get(id=idActividad)
    instancia.delete()
    return redirect('/tareas/welcome')

def editarSolicitud(request, idSolicitud):
    instancia = Solicitud.objects.get(id=idSolicitud)
    form = SolicitudFormEdicion(instance=instancia)
    context = {'form':form}
    if request.method == "POST":
        form = SolicitudFormEdicion(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            #mensaje= "El informe se modificó correctamente!"
            context = {'form':form}
            return redirect('/tareas/welcome')
    return render(request, 'tareas/editarSolicitud.html', context)

def listarGrupoAct(request, idGrupoActividad, *args, **kwargs):
    #Obtenemos el id del usuario logueado
    idU = User.objects.get(id=request.user.id)
    idUs = idU.id
    #Obtenemos las actividades relacionadas al usuario logueado
    actividades = Actividad.objects.filter(user=idUs)
    actividadesInforme = actividades.filter(grupoactividad_id=idGrupoActividad)
    context = {'actividadesInforme':actividadesInforme}
    return render(request, "tareas/listaGrupoAct.html", context)

def editarGrupoActividad(request, idGrupoActividad):
    instancia = GrupoActividad.objects.get(id=idGrupoActividad)
    actividades = Actividad.objects.filter(grupoactividad_id=idGrupoActividad)
    form = GrupoActividadForm(instance=instancia)
    context = {'form':form,'actividades':actividades,'instancia':instancia}
    if request.method == "POST":
        form = GrupoActividadForm(request.POST, instance=instancia)
        if form.is_valid():
            instancia = form.save(commit=False)
            instancia.save()
            #mensaje= "El informe se modificó correctamente!"
            context = {'form':form,'actividades':actividades,'instancia':instancia}
            return redirect('/tareas/welcome')
    return render(request, 'tareas/editarGrupoActividad.html', context)

def eliminarSolicitud(request, idSolicitud):
    instancia = Solicitud.objects.get(id=idSolicitud)
    instancia.delete()
    return redirect('/tareas/welcome')

def eliminarGrupoActividad(request, idGrupoActividad):
    actividades = Actividad.objects.filter(grupoactividad_id=idGrupoActividad)
    actividades.delete()
    #instancia = Solicitud.objects.get(id=idSolicitud)
    #instancia.delete()
    grupoActividad = GrupoActividad.objects.get(id=idGrupoActividad)
    grupoActividad.delete()
    return redirect('/tareas/welcome')
