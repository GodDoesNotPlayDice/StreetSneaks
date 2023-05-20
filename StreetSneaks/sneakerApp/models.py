from django.db import models

# Create your models here.
class Categoria(models.Model):
    pass

class Zapatilla(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    precio = models.IntegerField(default=0, verbose_name="Valor")
    talla = models.IntegerField(default=0, verbose_name="Talla")
    disponible = models.BooleanField(default=False, verbose_name="Disponible")
    tipo = models.CharField(max_length=15, verbose_name="Tipo")