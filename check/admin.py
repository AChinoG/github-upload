from django.contrib import admin

from .models import Notas, Categoria, CategoriaNota

admin.site.register(Notas)
admin.site.register(Categoria)
admin.site.register(CategoriaNota)

# Register your models here.
