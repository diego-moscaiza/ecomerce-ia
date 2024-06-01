from django.contrib import admin
from .models import Estante

class EstanteAdmin(admin.ModelAdmin):
    list_display = ('id_estante', 'id_inventario', 'numero_estante')

    # Mostrar el nombre del inventario en lugar de su ID
    # def id_inventario(self, obj):
    #     return obj.id_inventario.nombre
    # id_inventario.short_description = 'Inventario'

admin.site.register(Estante, EstanteAdmin)
