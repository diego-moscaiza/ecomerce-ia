from django.contrib import admin
from .models import Comprobante, TipoComprobante, Pedido


class ComprobanteAdmin(admin.ModelAdmin):
    list_display = (
        "id_comprobante",
        "id_tipo_comprobante",
        "id_pedido",
        "fecha",
        "importe",
    )
    search_fields = ("id_tipo_comprobante", "id_pedido", "fecha", "importe")
    list_filter = ("id_tipo_comprobante", "id_pedido", "fecha", "importe")

    # Si quieres mostrar el nombre del tipo de comprobante en lugar de su ID, puedes hacer lo siguiente:
    def id_tipo_comprobante(self, obj):
        return obj.id_tipo_comprobante.nombre

    id_tipo_comprobante.short_description = "Tipo de comprobante"

    # Si quieres mostrar el número de pedido en lugar de su ID, puedes hacer lo siguiente:
    def id_pedido(self, obj):
        return obj.id_pedido.numero

    id_pedido.short_description = "Número de pedido"


admin.site.register(Comprobante, ComprobanteAdmin)
