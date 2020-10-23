from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.models import AbstractUser

# Create your models here.

class No_usar(models.Model):
    ID_Usuario = models.AutoField(primary_key = True)
    name = models.CharField(max_length=30, blank=False, null=False)
    app = models.CharField(max_length=30, blank=False, null=False)
    apm = models.CharField(max_length=30, blank=False, null=False)
    correo = models.EmailField(max_length=254, blank=False, null=False)
    password = models.CharField(max_length=25, blank=False, null=False)
    #USERNAME_FIELD = 'correo'
    #REQUIRED_FIELDS = ['username']


class Categoria(models.Model):
    clasificacion = models.CharField(max_length=50, null=True)
    def __str__(self):
        return self.clasificacion
    

class Notas(models.Model):
    autor = models.CharField(max_length=50)
    tipo = models.ManyToManyField(Categoria, through='CategoriaNota')
    titulo = models.CharField(max_length=50)
    descrpcion = models.TextField(max_length=300)
    fecha = models.DateTimeField()
    usuario = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)


class CategoriaNota(models.Model):

    order_with_respect_to = 'Notas'

    unique_togeher = [
        ('Notas', 'Categoria'),
    ]

    clasificacion_choices = [
        (6, 'ORGANIZACION'),
        (11, 'TAREA'),
        (10, 'RECORDATORIO'),
        (9, 'IMPORTANTE'),
        (7, 'URGENTE'),
    ]

    nota = models.ForeignKey(Notas, models.CASCADE)
    clasificacion = models.ForeignKey(Categoria, models.CASCADE)
