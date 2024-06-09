from django.contrib import admin
from .models import Subcategoria

# Register your models here.

class SubcategoriaAdmin(admin.ModelAdmin):
    list_display = ('id_subcategoria', 'id_categoria', 'nombre_categoria', 'nombre', 'descripcion')

    def nombre_categoria(self, obj):
        return obj.id_categoria.nombre

admin.site.register(Subcategoria, SubcategoriaAdmin)
