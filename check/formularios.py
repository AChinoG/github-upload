from django import forms
from .models import Notas
from django.forms import ModelForm

class AddNota(ModelForm):
    class Meta:
        model = Notas
        fields = ['autor', 'titulo', 'descrpcion']


class Edit(ModelForm):
    class Meta:
        model = Notas
        fields = ['id','autor', 'titulo', 'descrpcion']