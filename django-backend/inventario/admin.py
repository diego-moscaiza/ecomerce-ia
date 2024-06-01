from django.contrib import admin
from .models import Inventario

class InventarioAdmin(admin.ModelAdmin):
    list_display = ('id_inventario', 'nombre')

admin.site.register(Inventario, InventarioAdmin)
