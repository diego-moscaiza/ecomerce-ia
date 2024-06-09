from django.db import models

# Create your models here.
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    id_proveedor = models.ForeignKey('proveedor.Proveedor', on_delete=models.CASCADE)
    id_subcategoria = models.ForeignKey('subcategoria.Subcategoria', on_delete=models.CASCADE, null=True, blank=True)
    id_estante = models.ForeignKey('estante.Estante', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50,null=True, blank=True)
    marca  = models.CharField(max_length=20, null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    descripcion = models.CharField(max_length=100, blank=True)
    cantidad = models.IntegerField(default=0)
    talla = models.CharField(max_length=5, null=True, blank=True)
    color = models.CharField(max_length=18, null=True, blank=True)
    genero = models.CharField(max_length=10, null=True, blank=True)
    estado = models.IntegerField(default=0)
    img = models.CharField(max_length=35, null=True, blank=True)
