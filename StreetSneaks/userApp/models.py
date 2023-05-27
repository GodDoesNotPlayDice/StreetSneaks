from django.db import models
from django.contrib.auth.models import User
from sneakerApp.models import Zapatilla

# Create your models here.
class Usuario(models.Model):
    email = models.EmailField(max_length=50, verbose_name="Email")
    celular = models.IntegerField(max_length=12, verbose_name="Celular")
    direccion = models.CharField(max_length=150, verbose_name="Direccion")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
