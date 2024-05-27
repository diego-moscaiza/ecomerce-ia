from rest_framework import serializers
from .models import Administrador

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrador
        fields = "__all__"