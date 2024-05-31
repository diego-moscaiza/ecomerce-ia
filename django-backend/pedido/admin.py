from django.contrib import admin
from .models import Pedido

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id_pedido', 'id_cliente', 'id_producto', 'costo', 'estado')

admin.site.register(Pedido, PedidoAdmin)
