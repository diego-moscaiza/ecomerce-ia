from django.db import models


class Proveedor(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    numero_ruc = models.CharField(max_length=11)
    nombre = models.CharField(max_length=40)
    representante = models.CharField(max_length=40)
    telefono_principal = models.CharField(max_length=9)
    telefono_secundario = models.CharField(max_length=9, blank=True)
    direccion = models.CharField(max_length=120)
    correo = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.nombre
