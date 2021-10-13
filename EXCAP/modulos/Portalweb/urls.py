from .views import formulario,acceder
from django.urls import path

urlpatterns = [
    #path('',index,name='index'),
    path('',formulario, name='formulario')
    
]
