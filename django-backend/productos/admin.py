from .models import Producto
from django.contrib import admin
from .reports import dowload_excel, dowload_pdf


class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        "id_producto",
        "nombre",
        "marca",
        "precio",
        "descripcion",
        "cantidad",
        "talla",
        "color",
        "genero",
        "estado",
        "nombre_proveedor",
        "nombre_subcategoria",
        "numero_estante",
    )
    search_fields = (
        "nombre",
        "marca",
        "precio",
        "descripcion",
        "cantidad",
        "talla",
        "color",
        "genero",
        "estado",
        "id_proveedor__nombre",
        "id_subcategoria__nombre",
        "id_estante__numero_estante",
    )
    list_filter = (
        "nombre",
        "marca",
        "precio",
        "descripcion",
        "cantidad",
        "talla",
        "color",
        "genero",
        "estado",
        "id_proveedor__nombre",
        "id_subcategoria__nombre",
        "id_estante__numero_estante",
    )

    def nombre_proveedor(self, obj):
        return obj.id_proveedor.nombre

    def nombre_subcategoria(self, obj):
        return obj.id_subcategoria.nombre

    def numero_estante(self, obj):
        return obj.id_estante.numero_estante

    actions = [dowload_excel, dowload_pdf]


dowload_excel.short_description = "Descargar Reporte en Excel"
dowload_pdf.short_description = "Descargar Reporte en PDF"


admin.site.register(Producto, ProductoAdmin)
