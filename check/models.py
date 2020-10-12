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


class Notas(models.Model):
    autor = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    descrpcion = models.TextField(max_length=300)
    fecha = models.DateTimeField()
    usuario = models.ForeignKey(User, models.SET_NULL, null=True, blank=True)


