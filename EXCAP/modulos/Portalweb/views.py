from django.shortcuts import render,redirect
import json
from .models import Usuario,Vips
from datetime import datetime,date

# Create your views here.
url=''
mac=''
dni=''
base_url=''
user_url=''
import requests

def alarma(datos):
    #card = '''{"type": "AdaptiveCard","body": [{"type": "ColumnSet","columns": [{"type": "Column","items": [{"type": "TextBlock","text": "MERBANK","weight": "Bolder","color": "Good","isSubtle": true},{"type": "TextBlock","weight": "Bolder","text": "INGRESO DE CLIENTE VIP","wrap": true,"color": "Light","size": "Large","spacing": "Small"}],"width": "stretch"}]},{"type": "ColumnSet","columns": [{"type": "Column","width": 35,"items": [{"type": "TextBlock","text": "Fecha","color": "Light"},{"type": "TextBlock","text": "Sede","weight": "Lighter","color": "Light","spacing": "Small"}]},{"type": "Column","width": 65,"items": [{"type": "TextBlock","text": "FECHA","color": "Light"},{"type": "TextBlock","text": "Webex Teams","color": "Light","weight": "Lighter","spacing": "Small"}]}],"spacing": "Padding","horizontalAlignment": "Center"},{"type": "TextBlock","text": "{} {}","wrap": true,"size": "Large","fontType": "Default","isSubtle": true,"weight": "Bolder","color": "Good"}],"$schema": "http://adaptivecards.io/schemas/adaptive-card.json","version": "1.2"}'''.format(datos.nombre,datos.apellidos)
    fecha = date.today()
    url_webex = "https://webexapis.com/v1/messages"
    true =  True
    payload = json.dumps({
    "roomId": "Y2lzY29zcGFyazovL3VzL1JPT00vOWQ4NmVlNzAtMWE3ZS0xMWVjLTliNzAtNTM1NjYyZTVkYzIz",
    "markdown" : "HA LLEGADO EL CLIENTE VIP: **{} {}**".format(datos.nombre,datos.apellidos),
    "attachments": [
            {
            "contentType": "application/vnd.microsoft.card.adaptive",
            "content": {
    "type": "AdaptiveCard",
    "body": [
        {
            "type": "ColumnSet",
            "columns": [
                {
                    "type": "Column",
                    "items": [
                        {
                            "type": "Image",
                            "url": "https://i.imgur.com/4Wb8As1.png",
                            "size": "Medium",
                            "height": "50px"
                        }
                    ],
                    "width": "auto"
                },
                {
                    "type": "Column",
                    "items": [
                        {
                            "type": "TextBlock",
                            "text": "MERBANK",
                            "weight": "Bolder",
                            "color": "Good",
                            "isSubtle": true
                        },
                        {
                            "type": "TextBlock",
                            "weight": "Bolder",
                            "text": "INGRESO DE CLIENTE VIP",
                            "wrap": true,
                            "color": "Light",
                            "size": "Large",
                            "spacing": "Small"
                        }
                    ],
                    "width": "stretch"
                }
            ]
        },
        {
            "type": "ColumnSet",
            "columns": [
                {
                    "type": "Column",
                    "width": 35,
                    "items": [
                        {
                            "type": "TextBlock",
                            "text": "Fecha",
                            "color": "Light"
                        },
                        {
                            "type": "TextBlock",
                            "text": "Sede",
                            "weight": "Lighter",
                            "color": "Light",
                            "spacing": "Small"
                        }
                    ]
                },
                {
                    "type": "Column",
                    "width": 65,
                    "items": [
                        {
                            "type": "TextBlock",
                            "text": "{}".format(fecha),
                            "color": "Light"
                        },
                        {
                            "type": "TextBlock",
                            "text": "Central",
                            "color": "Light",
                            "weight": "Lighter",
                            "spacing": "Small"
                        }
                    ]
                }
            ],
            "spacing": "Padding",
            "horizontalAlignment": "Center"
        },
        {
            "type": "TextBlock",
            "text": "- {} {}".format(datos.nombre,datos.apellidos),
            "wrap": true,
            "size": "Large",
            "fontType": "Default",
            "isSubtle": true,
            "weight": "Bolder",
            "color": "Good"
        }
    ],
    "$schema": "http://adaptivecards.io/schemas/adaptive-card.json",
    "version": "1.2"
}
                    

      }
    ]
    })
    headers = {
    'Authorization': 'Bearer YTg4OTVmYjktNWFkZS00YzA4LWFkNWItMjE5YTJkZDM1MjNmY2ZjOTFlZGItYmE1_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f',
    'Content-Type': 'application/json'
    }
    requests.request("POST", url_webex, headers=headers, data=payload)

def consulta_usuario_new(dni_v):
    if Vips.objects.filter(dni=dni_v):
        ulr_con='http://192.168.0.105:8080/vips/'
        usu_vip= Vips.objects.get(dni=dni_v)
        alarma(usu_vip)
    elif Usuario.objects.filter(dni=dni_v):
        print('antiguo')
        ulr_con='http://192.168.0.105:8080/antiguos/'
    else:
        print(' nuevo')
        ulr_con='http://192.168.0.105:8080/nuevos/'
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
    global mac,dni,continue_url,user_url
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
    global url,mac,dni,base_url,user_url
    #user_url=request.GET['user_continue_url']
    print('USER_URL: ',user_url,'\n','DNI: ',dni)
    
    url = base_url + '?continue_url=' + user_url + '&duration=60'
    print(url)
    #print('url',request.GET['user_continue_url'],)
    return render(request,'acceder.html',{'url_get':url})

def nuevos(request):
    return render(request,'nuevos.html')

def antiguos(request):
    return render(request,'antiguos.html')

def vips(request):
    return render(request,'vips.html')