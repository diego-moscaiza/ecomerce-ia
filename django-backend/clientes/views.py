from .models import Cliente
from .serializers import ClienteSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view(["POST"])
def login(request):
    correo_ingresado = request.data.get("correo")
    contraseña = request.data.get("contraseña")

    cliente = get_object_or_404(Cliente, correo=correo_ingresado)

    if not cliente.check_password(
        contraseña
    ):  # Use check_password to verify the password
        return Response(
            {"Error": "Contraseña inválida"}, status=status.HTTP_400_BAD_REQUEST
        )

    serializer = ClienteSerializer(instance=cliente)

    return Response({"cliente": serializer.data}, status=status.HTTP_200_OK)


@api_view(["POST"])
def register(request):
    serializer = ClienteSerializer(data=request.data)

    if serializer.is_valid():
        correo_ingresado = serializer.validated_data["correo"]
        contraseña = serializer.validated_data["contraseña"]

        if Cliente.objects.filter(correo=correo_ingresado).exists():
            return Response(
                {"Error": "El correo electrónico ya está registrado"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        cliente = serializer.save()
        cliente.set_password(contraseña)  # Hash the password
        cliente.save()  # Save the object after hashing the password

        return Response({"cliente": serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
