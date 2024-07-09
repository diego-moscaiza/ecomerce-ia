from rest_framework import serializers
from .models import InfoPrendasScraping


class InfoPrendasScrapingSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoPrendasScraping
        fields = [
            "nombre",
            "marca",
            "precio_oferta",
            "precio_normal",
            "genero",
            "imagen",
        ]
