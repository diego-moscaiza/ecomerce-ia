from django.contrib import admin
from .models import Subcategoria

# Register your models here.


class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = (
        "id_subcategoria",
        "nombre_categoria",
        "nombre",
        "descripcion",
    )
    search_fields = ("id_subcategoria", "id_categoria__nombre", "nombre", "descripcion")
    list_filter = ("id_categoria__nombre", "nombre")

    def nombre_categoria(self, obj):
        return obj.id_categoria.nombre


admin.site.register(Subcategoria, SubcategoriaAdmin)
