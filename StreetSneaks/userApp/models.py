from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Usuario(models.Model):
    celular = models.IntegerField(verbose_name="Celular")
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

class Region(models.Model):
    region = models.CharField(max_length=150, verbose_name="Regiones")


class Direccion(models.Model):
    direccion = models.CharField(max_length=150, verbose_name="Direccion", null=True)
    region = models.ForeignKey(Region, verbose_name="Region",on_delete=models.CASCADE,  null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Dirección"
        verbose_name_plural = "Direcciones"


    

# class Carro(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     items = models.JSONField(verbose_name="Items en el carrito", default=list)
 