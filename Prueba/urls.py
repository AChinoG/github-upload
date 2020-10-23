"""Prueba URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import login_required, logout_then_login 
from django.contrib.auth import views as auth_views
import check.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='index.html'), name="index"),
    path('', check.views.notas, name="inicio"),
    path('agregar/', check.views.add, name="agregar"),
    #path('buscar/', check.views.buscar, name="buscar"),
    path('eliminar/<int:id>/', check.views.eliminar, name="eliminar"),
    path('editar/<int:id>/', check.views.editar, name="editar"),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='index'), name="salir")
]
