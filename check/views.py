from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from check.models import Notas
from .formularios import AddNota, Edit
from django.contrib.auth import authenticate, login, logout
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required
def notas(request):
    if request.user.is_authenticated:
        nombre = request.user.id
        notas = Notas.objects.filter(usuario=nombre) 
        ctx = {
            'notas': notas,
        }
        return render(request, 'inicio.html', ctx)

@login_required
def eliminar(request, id):
    nota = Notas.objects.get(id=id)
    nota.delete()
    return redirect('inicio')

@login_required
def add(request): 
    form = AddNota()
    if request.method == 'POST':
        form = AddNota(data=request.POST)
        if form.is_valid():

            nota = form.save(commit=False)
            nota = Notas.objects.create(
                autor = form.cleaned_data['autor'],
                titulo = form.cleaned_data['titulo'],
                descrpcion = form.cleaned_data['descrpcion'],
                fecha = timezone.now(),
                usuario = request.user
            )
            
            nota.save()
            return redirect('inicio')

    return render(request, 'agregar.html', {'form':form})

def logout_sesion(request):
    logout(request)
    return render(request, 'index.html')

@login_required
def editar(request, id):
    edit = Notas.objects.get(id=id)
    form = Edit(instance=edit)
    if request.method == 'POST':
        form = Edit(data=request.POST, instance=edit)
        if form.is_valid():
            edit = form.save(commit=False)
            
            edit.autor = form.cleaned_data['autor']
            edit.titulo = form.cleaned_data['titulo']
            edit.descrpcion = form.cleaned_data['descrpcion']
            edit.fecha = timezone.now()

            edit.save()
            return redirect('inicio')

            
    return render(request, 'editar.html', {'form':form})