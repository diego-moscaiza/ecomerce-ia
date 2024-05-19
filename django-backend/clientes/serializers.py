from rest_framework import serializers
from .models import Cliente


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            "id_cliente",
            "nombre",
            "apellido",
            "documento",
            "fecha_nacimiento",
            "sexo",
            "telefono",
            "id_metodo_pago",
            "correo",
            "contraseña",
        ]
