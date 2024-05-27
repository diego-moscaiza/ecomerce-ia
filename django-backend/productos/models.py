from django.db import models

# Create your models here.
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    # id_inventario = models.ForeignKey('inventario.Inventario', on_delete=models.CASCADE)
    # id_proveedor = models.ForeignKey('proveedor.Proveedor', on_delete=models.CASCADE)
    # id_categoria = models.ForeignKey('categoria.Categoria', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, null=True)
    cantidad = models.IntegerField(default=0)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    estado = models.IntegerField(default=0)
    #img = models.ImageField(upload_to='products/')
