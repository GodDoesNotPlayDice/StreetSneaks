from django.db import models

# Create your models here.

class TallaEUR(models.Model):
    tipo = models.CharField(max_length=50, verbose_name="Tipo EUR", null=True, default='null')
    number = models.IntegerField(verbose_name="Número de talla", null=True)

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")

class Zapatilla(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    precio = models.IntegerField(default=0, verbose_name="Valor")
    disponible = models.BooleanField(default=False, verbose_name="Disponible")
    tallaEUR = models.ForeignKey(TallaEUR, on_delete=models.CASCADE, verbose_name="Talla EUR", null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoría")

