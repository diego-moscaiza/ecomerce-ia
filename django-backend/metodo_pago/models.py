from django.db import models


class MetodoPago(models.Model):
    id_metodo_pago = models.AutoField(primary_key=True)
    tipo = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.tipo
