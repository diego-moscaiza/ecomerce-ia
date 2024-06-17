from django.contrib import admin

from .models import InfoPrendasScraping

# Register your models here.


class InfoPrendasAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "nombre",
        "marca",
        "precio",
        "talla",
        "genero",
        "img",
    )
    search_fields = (
        "nombre",
        "marca",
        "precio",
        "talla",
        "genero",
    )
    list_filter = (
        "nombre",
        "marca",
        "precio",
        "talla",
        "genero",
    )


admin.site.register(InfoPrendasScraping, InfoPrendasAdmin)
