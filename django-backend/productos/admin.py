from django.contrib import admin
from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'nombre', 'descripcion', 'cantidad', 'precio', 'estado', 'proveedor_nombre', 'categoria_nombre', 'estante_nombre')

    def proveedor_nombre(self, obj):
        return obj.id_proveedor.nombre

    def categoria_nombre(self, obj):
        return obj.id_categoria.nombre

    def estante_nombre(self, obj):
        return obj.id_estante.nombre

admin.site.register(Producto, ProductoAdmin)
