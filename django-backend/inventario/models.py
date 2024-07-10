from django.db import models


class Inventario(models.Model):
    id_inventario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre
