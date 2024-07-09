from django.db import models


class InfoPrendasScraping(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=100, null=True, blank=True)
    precio_oferta = models.CharField(max_length=10, default="0.00")
    precio_normal = models.CharField(max_length=10, default="0.00")
    genero = models.CharField(max_length=10, null=True, blank=True)
    imagen = models.CharField(max_length=120, null=True, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)
