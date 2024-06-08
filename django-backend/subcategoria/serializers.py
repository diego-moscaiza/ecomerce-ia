from rest_framework import serializers
from .models import Subcategoria

class SubcategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategoria
        fields = "__all__"