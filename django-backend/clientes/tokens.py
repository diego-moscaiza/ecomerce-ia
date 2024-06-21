import os, binascii
from .models import Cliente
from django.db import models
from django.utils import timezone
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed


class ClienteToken(models.Model):
    cliente = models.OneToOneField(
        "Cliente", on_delete=models.CASCADE, related_name="token"
    )
    key = models.CharField(max_length=40, primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()

    def __str__(self):
        return self.key


class ClienteTokenAuthentication(TokenAuthentication):
    def authenticate(self, request):
        token = request.META.get("HTTP_AUTHORIZATION")
        if not token:
            return None

        try:
            token = token.split()[1]
            cliente = Cliente.objects.get(token=token)
            return (cliente, token)
        except Cliente.DoesNotExist:
            raise AuthenticationFailed("Invalid token")

    def authenticate_header(self, request):
        return "Bearer"

    def get_client_from_token(self, request):
        token = request.META.get("HTTP_AUTHORIZATION")
        if not token:
            return None

        try:
            token = token.split()[1]
            return Cliente.objects.get(token=token)
        except Cliente.DoesNotExist:
            return None

    def is_authenticated(self, request):
        return self.get_client_from_token(request) is not None

