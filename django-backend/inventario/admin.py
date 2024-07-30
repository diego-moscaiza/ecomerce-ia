from django.contrib import admin
from .models import Inventario, Estante


class InventarioAdmin(admin.ModelAdmin):
    list_display = ("id_inventario", "nombre")
    search_fields = ("nombre",)
    list_filter = ("nombre",)


class EstanteAdmin(admin.ModelAdmin):
    list_display = ("id_estante", "id_inventario", "numero_estante")
    search_fields = ("id_inventario", "numero_estante")
    list_filter = ("id_inventario", "numero_estante")


admin.site.register(Estante, EstanteAdmin)
admin.site.register(Inventario, InventarioAdmin)
