from django import forms
from tareas.models import Actividad, Solicitud, GrupoActividad

class ActividadForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100, required=True, help_text='*')
    comentarios = forms.CharField(max_length=100, required=False)

    class Meta:
        model = Actividad
        fields = ['nombre','comentarios','prioridad','grupoactividad']
        labels = {'nombre':'Nombre','comentarios':'Comentarios','prioridad':'Prioridad','grupoactividad':'Informe'}

class SolicitudForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100, required=True, help_text='*')

    class Meta:
        model = Solicitud
        fields = ['nombre','sector']
        labels = {'nombre':'Nombre','sector':'Sector'}

class GrupoActividadForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100, required=True, help_text='*')

    class Meta:
        model = GrupoActividad
        fields = ['nombre','prioridad']
        labels = {'nombre':'Nombre','prioridad':'Prioridad'}
