from django.db import models
from userApp.models import Carro
class Cupon(models.Model):
    name = models.CharField(max_length=255, verbose_name="Cupones")
    valor = models.IntegerField(null=True, verbose_name="Valor")

    class Meta:
        verbose_name = "Cupon"
        verbose_name_plural = "Cupones"
    
    def __str__(self) -> str:
        return self.name
    

class Iva(models.Model):
    valor = models.IntegerField(null=True, verbose_name="Valor")

    class Meta:
        verbose_name = "Iva"
        verbose_name_plural = "Ivas"
    
    def __str__(self) -> str:
        return str(self.valor)
    
class Boleta(models.Model):
    id_boleta = models.CharField(max_length=255, verbose_name="Id Boleta")
    productos = models.ForeignKey(Carro, on_delete=models.CASCADE, verbose_name="Productos")
    fecha = models.DateField(auto_now_add=True, verbose_name="Fecha")
    total = models.IntegerField(null=True, verbose_name="Total")
    iva = models.ForeignKey(Iva, on_delete=models.CASCADE, verbose_name="Iva")
    cupon = models.ForeignKey(Cupon, on_delete=models.CASCADE, verbose_name="Cupon")

    class Meta:
        verbose_name = "Boleta"
        verbose_name_plural = "Boletas"
    
    def __str__(self) -> str:
        return self.id_boleta