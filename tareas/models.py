from django.db import models
from django.contrib.auth.models import User

class Sector(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

class Estado(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Prioridad(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class GrupoActividad(models.Model):
    nombre = models.CharField(max_length=100)
    prioridad = models.ForeignKey(Prioridad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Actividad(models.Model):
    nombre = models.CharField(max_length=100)
    comentarios = models.CharField(max_length=200, blank=True, null=True)
    prioridad = models.ForeignKey(Prioridad, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    grupoactividad = models.ForeignKey(GrupoActividad, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return '%s %s %s' % (self.nombre, self.estado, self.grupoactividad)

class Solicitud(models.Model):
    nombre = models.CharField(max_length=100)
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s %s' % (self.nombre, self.actividad, self.sector, self.estado)
