from rest_framework import serializers
from .models import TipoComprobante

class TipoComprobanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoComprobante
        fields = "__all__"
