from django.db import models


class InfoPrendasScraping(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    marca = models.CharField(max_length=100, null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    talla = models.CharField(max_length=5, null=True, blank=True)
    genero = models.CharField(max_length=10, null=True, blank=True)
    img = models.CharField(max_length=225, null=True, blank=True)
    fecha = models.DateField(auto_now_add=True)
