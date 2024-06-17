from django.contrib import admin
from .models import Reembolso


class ReembolsoAdmin(admin.ModelAdmin):
    list_display = (
        "id_reembolso",
        "producto_nombre",
        "administrador_nombre",
        "cliente_nombre",
        "motivo",
        "cantidad",
        "metodo",
        "estado",
    )
    search_fields = (
        "id_reembolso",
        "producto_nombre",
        "administrador_nombre",
        "cliente_nombre",
        "motivo",
        "cantidad",
        "metodo",
        "estado",
    )
    list_filter = (
        "id_reembolso",
        "id_producto__nombre",
        "id_administrador__nombre",
        "id_cliente__nombre",
        "motivo",
        "cantidad",
        "metodo",
        "estado",
    )

    def producto_nombre(self, obj):
        return obj.id_producto.nombre

    def administrador_nombre(self, obj):
        return obj.id_administrador.nombre

    def cliente_nombre(self, obj):
        return obj.id_cliente.nombre


admin.site.register(Reembolso, ReembolsoAdmin)
