from django.db import models

# Create your models here.
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    # id_inventario = models.IntegerField(null=True)
    # id_proveedor = models.IntegerField(null=True)
    # id_categoria = models.IntegerField(null=True)
    nombre = models.CharField(max_length=50, null=True)
    descripcion = models.CharField(max_length=100, null=True)
    cantidad = models.IntegerField(null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    estado = models.CharField(max_length=1, null=True)
    
    