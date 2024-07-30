from rest_framework import serializers
from .models import Inventario, Estante


class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = "__all__"


class EstanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estante
        fields = "__all__"
