from django.db import models
class Cupon(models.Model):
    name = models.CharField(max_length=255, verbose_name="Cupones")
    valor = models.IntegerField(null=True, verbose_name="Valor")

class Iva(models.Model):
    valor = models.IntegerField(null=True, verbose_name="Valor")