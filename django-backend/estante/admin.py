from django.contrib import admin
from .models import Estante


class EstanteAdmin(admin.ModelAdmin):
    list_display = ("id_estante", "id_inventario", "numero_estante")
    search_fields = ("id_inventario", "numero_estante")
    list_filter = ("id_inventario", "numero_estante")


admin.site.register(Estante, EstanteAdmin)
