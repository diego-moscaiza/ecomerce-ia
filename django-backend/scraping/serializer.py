from rest_framework import serializers

from .models import InfoPrendasScraping


class RopaScrapingSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoPrendasScraping
        fields = "__all__"
