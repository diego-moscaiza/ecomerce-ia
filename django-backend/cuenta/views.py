from django.utils import timezone
from django.contrib.auth.models import User
from .serializers import CuentaSerializer
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(["POST"])
def register(request):
    serializer = CuentaSerializer(data=request.data)

    if serializer.is_valid():
        user_email = serializer.validated_data["email"]
        user_name = serializer.validated_data["username"]
        user_password = serializer.validated_data["password"]

        if User.objects.filter(username=user_name).exists():
            return Response(
                {"Error": "El nombre de usuario ya está registrado"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if User.objects.filter(email=user_email).exists():
            return Response(
                {"Error": "El correo electrónico ya está registrado"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = serializer.save()
        user.set_password(user_password)
        user.save()

        token = Token.objects.create(user=user)

        return Response(
            {"token": token.key, "user": serializer.data},
            status=status.HTTP_201_CREATED,
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def login_user(request):
    user_name = request.data.get("username")
    user_password = request.data.get("password")

    user = get_object_or_404(User, username=user_name)

    if user.is_staff:
        return Response(
            {"Error": "No es un usuario válido"},
            status=status.HTTP_403_FORBIDDEN,
        )

    if not user.check_password(user_password):
        return Response(
            {"Error": "Contraseña inválida"}, status=status.HTTP_400_BAD_REQUEST
        )

    user.last_login = timezone.now()
    user.save()

    token, created = Token.objects.get_or_create(user=user)
    serializer = CuentaSerializer(instance=user)

    return Response(
        {"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK
    )


@api_view(["POST"])
def login_admin(request):
    admin_name = request.data.get("username")
    admin_password = request.data.get("password")

    admin_user = get_object_or_404(User, username=admin_name)

    if not admin_user.is_staff:
        return Response(
            {"Error": "No tienes permiso para acceder a este sitio"},
            status=status.HTTP_403_FORBIDDEN,
        )
    else:
        if not admin_user.check_password(admin_password):
            return Response(
                {"Error": "Usuario o contraseña inválida"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        admin_user.last_login = timezone.now()
        admin_user.save()
        token, created = Token.objects.get_or_create(user=admin_user)
        serializer = CuentaSerializer(instance=admin_user)
    return Response(
        {"token": token.key, "user": serializer.data}, status=status.HTTP_200_OK
    )


@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    serializer = CuentaSerializer(instance=request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def logout(request):
    token = request.headers.get("Authorization")
    if token:
        token = token.split(" ")[1]  # Extraer el token de la cabecera
        token_obj = Token.objects.filter(key=token).first()
        if token_obj:
            token_obj.delete()
            return Response(
                {"Message": "Haz cerrado sesión"}, status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"Error": "Token no válido"}, status=status.HTTP_401_UNAUTHORIZED
            )
    else:
        return Response(
            {"Error": "No se proporcionó un token"}, status=status.HTTP_401_UNAUTHORIZED
        )
