from django.contrib import admin
from .models import Pedido


class PedidoAdmin(admin.ModelAdmin):
    list_display = (
        "id_pedido",
        "id_cliente",
        "id_producto",
        "costo",
        "estado",
    )
    search_fields = ("id_cliente", "id_producto", "costo", "estado")
    list_filter = ("id_cliente", "id_producto", "estado")


admin.site.register(Pedido, PedidoAdmin)
