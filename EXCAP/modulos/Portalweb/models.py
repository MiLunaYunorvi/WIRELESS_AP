from django.db import models

# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=64)
    apellidos = models.CharField(max_length=64)
    email=models.EmailField()
    dni=models.IntegerField()
    mac=models.CharField(max_length=64)
    tiempo=models.CharField(max_length=64)

class Vips(models.Model):
    nombre = models.CharField(max_length=64)
    apellidos = models.CharField(max_length=64)
    email=models.EmailField()
    dni=models.IntegerField()