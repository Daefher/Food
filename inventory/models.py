from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class categoria(models.Model):
    nombre = models.CharField(max_length=64, null=True)

    def __str__(self):
        return self.nombre

class articulo(models.Model):
    nombre = models.CharField(max_length=64, null=True)
    cantidad = models.IntegerField(null=True)
    slug = models.SlugField(max_length=128, null=True)
    #imagen = models.ImageField(null=True)
    categoria = models.ForeignKey(categoria, on_delete=models.CASCADE, blank=True)
    fecha_creacion = models.DateField(null=True)
    user = models.ForeignKey(User, on_delete=True, blank=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse("inventory:list-view")
    


    