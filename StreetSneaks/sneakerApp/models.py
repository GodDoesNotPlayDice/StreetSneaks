from django.db import models
# Create your models here.

class TallaEUR(models.Model):
    tipo = models.CharField(max_length=50, verbose_name="Tipo EUR", null=True, default='null')
    number = models.IntegerField(verbose_name="Número de talla", null=True)
    
    class Meta:
        verbose_name = "Talla EUR"
        verbose_name_plural = "Tallas EUR"

    def __str__(self) -> str:
        return str(self.number)
    

class Categoria(models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
    
    def __str__(self) -> str:
        return self.nombre
    

class Zapatilla(models.Model):
    id_prod = models.CharField(max_length=50, verbose_name="ID", unique=True, null=True)
    name = models.CharField(max_length=50, verbose_name="Nombre")
    imagen = models.ImageField(verbose_name="Imagen", default="null", upload_to="zapatillas")
    imagen_muestra = models.ImageField(verbose_name="Imagen muestra", default="null", blank=True, upload_to="imagen")
    imagen_muestra_2 = models.ImageField(verbose_name="Imagen muestra", default="null", blank=True, upload_to="imagen")
    precio = models.IntegerField(default=0, verbose_name="Valor")
    disponible = models.BooleanField(default=False, verbose_name="Disponible")
    tallaEUR = models.ForeignKey(TallaEUR, on_delete=models.CASCADE, verbose_name="Talla EUR", null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoría")
    
    class Meta:
        verbose_name = "Zapatilla"
        verbose_name_plural = "Zapatillas"

    def __str__(self) -> str:
        return self.name
    
