from django.contrib import admin
from .models import Entrega


class EntregaAdmin(admin.ModelAdmin):
    list_display = (
        "id_proveedor",
        "id_producto",
        "cantidad_entregada",
        "fecha_entrega",
    )
    list_filter = ("id_proveedor", "id_producto")

    # def has_add_permission(self, request):
    #     return False

    def has_change_permission(self, request, obj=None):
        return False


admin.site.register(Entrega, EntregaAdmin)
