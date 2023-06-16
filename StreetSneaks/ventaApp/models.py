from django.db import models
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
    