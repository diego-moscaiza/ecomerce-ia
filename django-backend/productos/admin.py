from django.contrib import admin
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'nombre', 'marca', 'precio', 'descripcion', 'cantidad', 'talla', 'color', 'genero', 'estado', 'nombre_proveedor', 'nombre_subcategoria', 'numero_estante')

    def nombre_proveedor(self, obj):
        return obj.id_proveedor.nombre

    def nombre_subcategoria(self, obj):
        return obj.id_subcategoria.nombre

    def numero_estante(self, obj):
        return obj.id_estante.numero_estante

admin.site.register(Producto, ProductoAdmin)
