from django.shortcuts import render
from . import views
from datetime import date

def home(request):
    fecha = date.today()
    context = {'fecha':fecha}
    return render(request, 'home.html', context)
