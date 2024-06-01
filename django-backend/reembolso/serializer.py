from rest_framework import serializers
from .models import Reembolso

class ReembolsoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reembolso
        fields = "__all__"
