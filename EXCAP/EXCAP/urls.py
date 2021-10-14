"""EXCAP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls.conf import include
from modulos.Portalweb.views import formulario,registrar,acceder,lista,nuevos,antiguos,vips,lista_clientes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registrar/',registrar),
    path('acceder/',acceder,name='acceder'),
    path('lista/',lista,name="lista"),
    path('',formulario,name='formulario'),
    path('formulario/',include('modulos.Portalweb.urls'),name='formulario'),
    path('nuevos/',nuevos,name='nuevos'),
    path('vips/',vips,name='vips'),
    path('antiguos/',antiguos,name='antiguos'),
    path('listaclientes/',lista_clientes,name='lista_clientes')]