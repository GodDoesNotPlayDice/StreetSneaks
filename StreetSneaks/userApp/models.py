from django.db import models

# Create your models here.
class Usuario(models.Model):
    name = models.CharField(max_length=15, verbose_name="Nombre")
    last_name = models.CharField(max_length=15, verbose_name="Apellido")
    email = models.EmailField(max_length=50, verbose_name="Email")
    password = models.CharField(max_length=50, verbose_name="Password")
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

