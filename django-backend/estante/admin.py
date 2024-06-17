from django.contrib import admin
from .models import Estante


class EstanteAdmin(admin.ModelAdmin):
    list_display = ("id_estante", "nombre_inventario", "numero_estante")
    search_fields = ("id_inventario", "numero_estante")
    list_filter = ("id_inventario", "numero_estante")

    # Mostrar el nombre del inventario en lugar de su ID
    def nombre_inventario(self, obj):
        return obj.id_inventario.nombre


admin.site.register(Estante, EstanteAdmin)
