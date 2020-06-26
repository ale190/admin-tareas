from django.shortcuts import render
from django.http import HttpResponse
from . models import Prioridad

def lista_prioridad(request):
    prioridad = Prioridad.objects.all()
    response = ', '.join([str(p) for p in prioridad])
    return HttpResponse(response)
