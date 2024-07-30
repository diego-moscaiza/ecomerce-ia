from django.db import models
from pedido.models import Pedido
from tipo_comprobante.models import TipoComprobante


class Comprobante(models.Model):
    id_comprobante = models.AutoField(primary_key=True)
    id_tipo_comprobante = models.ForeignKey(TipoComprobante, on_delete=models.SET_NULL, null=True)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    importe = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.id_comprobante
