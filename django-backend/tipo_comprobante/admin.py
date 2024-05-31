from django.contrib import admin
from .models import TipoComprobante

class TipoComprobanteAdmin(admin.ModelAdmin):
    list_display = ('id_tipo_comprobante', 'nombre')

admin.site.register(TipoComprobante, TipoComprobanteAdmin)
