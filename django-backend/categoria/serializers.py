from rest_framework import serializers
from .models import Categoria

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"