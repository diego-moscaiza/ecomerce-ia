from django.db import models


class Entrega(models.Model):
    id_entrega = models.AutoField(primary_key=True)
    id_proveedor = models.ForeignKey("proveedor.Proveedor", on_delete=models.SET_NULL, null=True)
    id_producto = models.ForeignKey("productos.Producto", on_delete=models.SET_NULL, null=True)
    cantidad_entregada = models.IntegerField(default=0)
    fecha_entrega = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.id_proveedor.nombre
