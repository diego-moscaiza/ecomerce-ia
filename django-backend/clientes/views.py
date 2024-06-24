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
from rest_framework.exceptions import AuthenticationFailed


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

    # Eliminar token anterior
    ClienteToken.objects.filter(cliente=cliente).delete()

    # Generar nuevo token
    token, created = ClienteToken.objects.get_or_create(cliente=cliente)

    serializer = ClienteSerializer(instance=cliente)

    return Response(
        {"token": token.key, "cliente": serializer.data}, status=status.HTTP_200_OK
    )


@api_view(["POST"])
@authentication_classes([ClienteTokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    cliente = request.user
    serializer = ClienteSerializer(instance=cliente)
    message = f"Estás logueado con {cliente.correo}"
    return Response((message, serializer.data), status=status.HTTP_200_OK)


@api_view(["POST"])
@authentication_classes([ClienteTokenAuthentication])
def logout(request):
    if request.user.is_authenticated:
        try:
            token = request.auth  # Obtener el token autenticado
            cliente_token = ClienteToken.objects.get(key=token)
            cliente_token.delete()  # Eliminar el token del cliente
            return Response(
                {"message": "You are now logged out."}, status=status.HTTP_200_OK
            )
        except ClienteToken.DoesNotExist:
            return Response(
                {"message": "Token not found."}, status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"message": "Error logging out.", "error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
    else:
        return Response(
            {"message": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED
        )
