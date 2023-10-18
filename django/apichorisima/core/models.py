from django.db import models

# Create your models here.

class user(models.Model):
    correo = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

class holahola1234(models.Model):
    correo = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)