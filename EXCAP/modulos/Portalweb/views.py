from django.shortcuts import render,redirect
import json
from .models import Usuario
from datetime import datetime

# Create your views here.
url=''
mac=''



def lista(request):
    usuariosenlista=Usuario.objects.all()
    print(usuariosenlista)
    return render(request,'usuarios.html',{"usuarios":usuariosenlista})

def formulario(request):
    global url,mac
    user_url=request.GET['user_continue_url']
    base_url=request.GET['base_grant_url']
    mac=request.GET['client_mac']
    url = base_url + '?continue_url=' + user_url + '&duration=120'
    print(url)
    print('url',request.GET['user_continue_url'],)
    return render (request, 'formulario.html')

def registrar(request):
    global mac
    tiempo=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    nombre=request.POST['nombres']
    apellidos=request.POST['apellidos']
    dni=request.POST['dni']
    email=request.POST['email']
    print(datetime)
    usuario= Usuario.objects.create(nombre=nombre, apellidos=apellidos, dni=dni, email=email,mac=mac,tiempo=str(tiempo))
    return redirect('/acceder')

def acceder(request):
    global url
    return render(request,'acceder.html',{'url_get':url})