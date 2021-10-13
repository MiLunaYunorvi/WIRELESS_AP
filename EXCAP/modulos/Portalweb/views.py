from django.shortcuts import render,redirect
import json
from .models import Usuario
from datetime import datetime

# Create your views here.
url=''
mac=''
dni=''
base_url=''

def consulta_usuario_new(dni_v):
    if Usuario.objects.filter(dni=dni_v):
        print('va al BCP')
        ulr_con='https://www.viabcp.com/'
    else:
        print('va al bbva, nuevo')
        ulr_con='www.bbva.pe'
    return ulr_con


def lista(request):
    usuariosenlista=Usuario.objects.all()
    print(usuariosenlista)
    return render(request,'usuarios.html',{"usuarios":usuariosenlista})

def formulario(request):
    global mac,base_url
    base_url=request.GET['base_grant_url']
    mac=request.GET['client_mac']
    return render (request, 'formulario.html')

def registrar(request):
    global mac,dni,continue_url
    tiempo=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    nombre=request.POST['nombres']
    apellidos=request.POST['apellidos']
    dni=request.POST['dni']
    email=request.POST['email']
    print(datetime)
    user_url=consulta_usuario_new(dni)
    usuario= Usuario.objects.create(nombre=nombre, apellidos=apellidos, dni=dni, email=email,mac=mac,tiempo=str(tiempo))
    return redirect('/acceder')

def acceder(request):
    global url,mac,dni,base_url
    #user_url=request.GET['user_continue_url']
    print('BASE_URL: ',base_url,'\n','DNI: ',dni)
    
    url = base_url + '?continue_url=' + user_url + '&duration=120'
    print(url)
    #print('url',request.GET['user_continue_url'],)
    return render(request,'acceder.html',{'url_get':url})