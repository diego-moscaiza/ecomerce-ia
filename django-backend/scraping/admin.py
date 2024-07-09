from .reports import dowload_excel, dowload_pdf
from .models import InfoPrendasScraping
from django.contrib import admin


class InfoPrendasAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nombre",
        "marca",
        "precio_oferta",
        "precio_normal",
        "genero",
        "imagen",
    )
    search_fields = (
        "nombre",
        "marca",
        "precio_oferta",
        "precio_normal",
        "genero",
        "imagen",
    )
    list_filter = (
        "nombre",
        "marca",
        "precio_oferta",
        "precio_normal",
        "genero",
        "imagen",
    )

    actions = [dowload_excel, dowload_pdf]


admin.site.register(InfoPrendasScraping, InfoPrendasAdmin)

dowload_excel.short_description = "Descargar Reporte en Excel"
dowload_pdf.short_description = "Descargar Reporte en PDF"
