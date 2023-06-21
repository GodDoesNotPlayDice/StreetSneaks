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
    
class Venta(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario" , null=True)
    items = models.ForeignKey('sneakerApp.Zapatilla', on_delete=models.CASCADE, verbose_name="Producto")
    cupon = models.ForeignKey(Cupon, on_delete=models.CASCADE, verbose_name="Cupon", null=True)
    direccion = models.ForeignKey('userApp.Direccion', on_delete=models.CASCADE, verbose_name="Direccion", null=True)


class Boleta(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario" , null=True)
    id_boleta = models.CharField(max_length=255, verbose_name="Id Boleta")
    productos = models.ForeignKey(Venta, on_delete=models.CASCADE, verbose_name="Productos", null=True)
    fecha = models.CharField(max_length=255, verbose_name="Fecha Entrega")
    fecha_actual = models.DateField(auto_now=True, verbose_name="Fecha Actual")
    total = models.IntegerField(null=True, verbose_name="Total")
    iva = models.IntegerField(null=True, verbose_name="Iva")
    descuento = models.IntegerField(null=True, verbose_name="Descuento")
    numero_tarjeta = models.CharField(max_length=255, verbose_name="Numero Tarjeta", null=True)

    class Meta:
        verbose_name = "Boleta"
        verbose_name_plural = "Boletas"
    
    def __str__(self) -> str:
        return self.id_boleta
    

