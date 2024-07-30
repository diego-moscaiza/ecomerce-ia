from django.db import models


class Inventario(models.Model):
    id_inventario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Estante(models.Model):
    id_estante = models.AutoField(primary_key=True)
    id_inventario = models.ForeignKey(Inventario, on_delete=models.SET_NULL, null=True)
    numero_estante = models.IntegerField()

    def __str__(self):
        return self.nombre