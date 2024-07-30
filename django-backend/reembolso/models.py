from django.db import models
from productos.models import Producto
from administrador.models import Administrador
from clientes.models import Cliente

class Reembolso(models.Model):
    id_reembolso = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    id_administrador = models.ForeignKey(Administrador, on_delete=models.SET_NULL, null=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    motivo = models.CharField(max_length=120)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    metodo = models.CharField(max_length=50)
    estado = models.CharField(max_length=1)
