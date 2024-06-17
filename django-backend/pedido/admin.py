from django.contrib import admin
from .models import Pedido


class PedidoAdmin(admin.ModelAdmin):
    list_display = (
        "id_pedido",
        "id_cliente",
        "nombre_cliente",
        "id_producto",
        "nombre_producto",
        "costo",
        "estado",
    )
    search_fields = ("nombre_cliente", "nombre_producto", "estado")
    list_filter = ("id_cliente__nombre", "id_producto__nombre", "estado")

    def nombre_cliente(self, obj):
        return obj.id_cliente.nombre

    def nombre_producto(self, obj):
        return obj.id_producto.nombre


admin.site.register(Pedido, PedidoAdmin)
