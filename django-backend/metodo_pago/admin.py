from django.contrib import admin
from .models import MetodoPago

class MetodoPagoAdmin(admin.ModelAdmin):
    list_display = ('id_metodo_pago', 'tipo')

admin.site.register(MetodoPago, MetodoPagoAdmin)
