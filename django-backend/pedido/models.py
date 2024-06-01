from django.db import models
from clientes.models import Cliente
from productos.models import Producto

class Pedido(models.Model):
    id_pedido = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, blank=True, null=True)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, blank=True, null=True)
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=1)
