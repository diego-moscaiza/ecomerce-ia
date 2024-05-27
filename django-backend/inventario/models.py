from django.db import models

class Inventario(models.Model):
    id_inventario = models.AutoField(primary_key=True)
    ubicacion = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    estado = models.CharField(max_length=1)
