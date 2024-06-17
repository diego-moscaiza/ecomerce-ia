from django.contrib import admin
from .models import Proveedor


class ProveedorAdmin(admin.ModelAdmin):
    list_display = (
        "id_proveedor",
        "numero_ruc",
        "nombre",
        "representante",
        "telefono_principal",
        "telefono_secundario",
        "direccion",
        "correo",
    )
    search_fields = (
        "numero_ruc",
        "nombre",
        "representante",
        "telefono_principal",
        "telefono_secundario",
        "direccion",
        "correo",
    )
    list_filter = (
        "numero_ruc",
        "nombre",
        "representante",
        "telefono_principal",
        "telefono_secundario",
        "direccion",
        "correo",
    )


admin.site.register(Proveedor, ProveedorAdmin)
