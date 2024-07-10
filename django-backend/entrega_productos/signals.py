from .models import Entrega
from productos.models import Producto
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import F


@receiver(post_save, sender=Entrega)
def incrementar_cantidad_producto(sender, instance, created, **kwargs):
    if created:
        producto_id = instance.id_producto_id
        cantidad_entregada = instance.cantidad_entregada
        Producto.objects.filter(id_producto=producto_id).update(
            cantidad=F("cantidad") + cantidad_entregada
        )
