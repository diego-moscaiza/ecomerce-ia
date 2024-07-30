from django.db import models


class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return self.nombre


class Subcategoria(models.Model):
    id_subcategoria = models.AutoField(primary_key=True)
    id_categoria = models.ForeignKey("Categoria", on_delete=models.SET_NULL, null=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=60, null=True, blank=True)

    def __str__(self):
        return self.nombre
