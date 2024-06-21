from .models import Cliente
from .tokens import ClienteToken, ClienteTokenAuthentication
from .serializers import ClienteSerializer
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


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
        cliente.set_password(contraseña)
        cliente.save()

        token = ClienteToken.objects.create(cliente=cliente)

        return Response(
            {"token": token.key, "cliente": serializer.data},
            status=status.HTTP_201_CREATED,
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login(request):
    correo_ingresado = request.data.get("correo")
    contraseña = request.data.get("contraseña")

    cliente = get_object_or_404(Cliente, correo=correo_ingresado)

    if not cliente.check_password(contraseña):
        return Response(
            {"Error": "Contraseña inválida"}, status=status.HTTP_400_BAD_REQUEST
        )

    token, created = ClienteToken.objects.get_or_create(cliente=cliente)
    serializer = ClienteSerializer(instance=cliente)

    return Response(
        {"token": token.key, "cliente": serializer.data}, status=status.HTTP_200_OK
    )


@api_view(["POST"])
def logout(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            request.user.auth_token.delete()
        return Response({"message": "Estás desconectado"}, status=status.HTTP_200_OK)


@api_view(["POST"])
@authentication_classes([ClienteTokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    cliente = get_cliente_from_database(request)
    if cliente:
        serializer = ClienteSerializer(instance=cliente)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(
            {"Error": "Cliente no encontrado"}, status=status.HTTP_404_NOT_FOUND
        )


def get_cliente_from_database(request):
    user = request.user
    if user.is_authenticated:
        return user  # Return the Client object itself
    else:
        return None


class ClienteMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        cliente = get_cliente_from_database(request)
        request.cliente = cliente
        response = self.get_response(request)
        return response
