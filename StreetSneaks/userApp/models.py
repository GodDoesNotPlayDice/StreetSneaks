from django.db import models
from django.contrib.auth.models import User
from sneakerApp.models import Zapatilla
from ventaApp.models import Cupon
# Create your models here.

class Usuario(models.Model):
    celular = models.IntegerField(verbose_name="Celular")
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
    
    def __str__(self) -> str:
        return self.user.username
    

class Region(models.Model):
    region = models.CharField(max_length=150, verbose_name="Regiones")

    class Meta:
        verbose_name = "Región"
        verbose_name_plural = "Regiones"
    
    def __str__(self) -> str:
        return self.region


class Direccion(models.Model):
    direccion = models.CharField(max_length=150, verbose_name="Direccion", null=True)
    region = models.ForeignKey(Region, verbose_name="Region",on_delete=models.CASCADE,  null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Dirección"
        verbose_name_plural = "Direcciones"

    def __str__(self) -> str:
        return self.direccion
    


class Carro(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ForeignKey(Zapatilla, on_delete=models.CASCADE)
    cupon = models.ForeignKey(Cupon, on_delete=models.CASCADE, null=True)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Carro"
        verbose_name_plural = "Carros"

    def __str__(self) -> str:
        return self.user.username


class Tarjeta(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    numero = models.IntegerField(verbose_name="Numero")
    fecha_vencimiento = models.DateField(verbose_name="Fecha de vencimiento")
    cvv = models.IntegerField(verbose_name="CVV")
    
    


 