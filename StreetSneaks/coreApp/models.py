from django.db import models

# Create your models here.
class Contactanos(models.Model):
    nombre = models.CharField(max_length=200)
    surname = models.CharField(max_length=200, null=True, blank=True)
    celular = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200)
    nro_pedido = models.CharField(max_length=200 , null=True, blank=True)
    asunto = models.CharField(max_length=200, null=True, blank=True)
    mensaje = models.CharField(max_length=1000, null=True, blank=True)
    propuesta = models.CharField(max_length=1000, null=True, blank=True)
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Contactanos"
