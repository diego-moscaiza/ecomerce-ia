from django.contrib import admin
from .models import Categoria, Subcategoria


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id_categoria", "nombre", "descripcion")
    search_fields = ("nombre", "descripcion")
    list_filter = ("nombre", "descripcion")


class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = (
        "id_subcategoria",
        "id_categoria",
        "nombre",
        "descripcion",
    )
    search_fields = ("id_subcategoria", "id_categoria", "nombre", "descripcion")
    list_filter = ("id_categoria", "nombre")


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Subcategoria, SubcategoriaAdmin)
