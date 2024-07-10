from django.db import models


class TipoComprobante(models.Model):
    id_tipo_comprobante = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return self.nombre
