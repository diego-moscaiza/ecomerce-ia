from rest_framework import serializers
from .models import Estante

class EstanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estante
        fields = "__all__"