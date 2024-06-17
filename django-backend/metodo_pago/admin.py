from django.contrib import admin
from .models import MetodoPago


class MetodoPagoAdmin(admin.ModelAdmin):
    list_display = ("id_metodo_pago", "tipo")
    search_fields = ("tipo",)
    list_filter = ("tipo",)


admin.site.register(MetodoPago, MetodoPagoAdmin)
