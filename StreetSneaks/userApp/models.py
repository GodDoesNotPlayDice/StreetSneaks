from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Usuario(models.Model):
    celular = models.IntegerField(verbose_name="Celular")
    direccion = models.CharField(max_length=150, verbose_name="Direccion", null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
