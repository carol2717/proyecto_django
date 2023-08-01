from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(
            default=timezone.now)
    fecha_publicacion = models.DateTimeField(
            blank=True, null=True)
    
class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_creacion = models.DateTimeField(
            default=timezone.now)
    fecha_publicacion = models.DateTimeField(
            blank=True, null=True)
    
class Estudiante(models.Model):
    nombre = models.CharField(max_length=200)
    cedula = models.TextField()
    fecha_creacion = models.DateTimeField(
            default=timezone.now)


