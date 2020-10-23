from django import forms
from .models import Notas, Categoria, CategoriaNota
from django.forms import ModelForm
from django.forms.widgets import CheckboxSelectMultiple

class AddNota(ModelForm):
    tipo = forms.MultipleChoiceField(
        required=True,
        label='Categoria',
        widget=forms.CheckboxSelectMultiple,
        choices=CategoriaNota.clasificacion_choices,
    )
    class Meta:
        model = Notas
        fields = ['titulo', 'tipo', 'autor', 'descrpcion']


class Edit(ModelForm):
    tipo = forms.MultipleChoiceField(
        required=False,
        label='Categoria',
        widget=CheckboxSelectMultiple(),
        choices=CategoriaNota.clasificacion_choices,
    )
    class Meta:
        model = Notas
        fields = ['id','titulo', 'tipo', 'autor', 'descrpcion']

class Filtro(ModelForm):
    class Meta:
        model = Notas
        fields = ['tipo']