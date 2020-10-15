from django import forms
from .models import Notas, Categoria
from django.forms import ModelForm

class AddNota(ModelForm):
    class Meta:
        model = Notas
        fields = ['titulo', 'tipo', 'autor', 'descrpcion']


class Edit(ModelForm):
    class Meta:
        model = Notas
        fields = ['id','titulo', 'tipo', 'autor', 'descrpcion']