from django.contrib import admin
from .models import Categoria

# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("id_categoria", "nombre", "descripcion")
    search_fields = ("nombre", "descripcion")
    list_filter = ("nombre", "descripcion")


admin.site.register(Categoria, CategoriaAdmin)
