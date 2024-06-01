from django.contrib import admin
from .models import Cliente

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id_cliente', 'nombre', 'apellido', 'documento', 'fecha_nacimiento', 'sexo', 'telefono', 'id_metodo_pago', 'correo')

admin.site.register(Cliente, ClienteAdmin)
