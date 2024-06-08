from django.db import models

class Subcategoria(models.Model):
    id_subcategoria = models.AutoField(primary_key=True)
    id_categoria = models.ForeignKey('categoria.Categoria', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=60, null=True, blank=True)
