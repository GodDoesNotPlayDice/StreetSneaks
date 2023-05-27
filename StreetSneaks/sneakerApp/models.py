from django.db import models

# Create your models here.

class Talla(models.Model):
    tipo = models.CharField(max_length=50, verbose_name="Tipo US/EUR")
    number = models.IntegerField(verbose_name="Número de talla")

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")

class Zapatilla(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    precio = models.IntegerField(default=0, verbose_name="Valor")
    disponible = models.BooleanField(default=False, verbose_name="Disponible")
    talla = models.ForeignKey(Talla, on_delete=models.CASCADE, verbose_name="Talla")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoría")

