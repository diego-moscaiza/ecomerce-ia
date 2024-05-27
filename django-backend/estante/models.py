from django.db import models

class Estante(models.Model):
    id_estante = models.AutoField(primary_key=True)
    id_inventario = models.ForeignKey('inventario.Inventario', on_delete=models.CASCADE)
    numero_estante = models.IntegerField()
