import os, binascii
from clientes.models import Cliente
from django.db import models
from django.utils import timezone
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import TokenAuthentication


class ClienteToken(models.Model):
    cliente = models.OneToOneField(
        Cliente, on_delete=models.CASCADE, related_name="token"
    )
    key = models.CharField(max_length=40, primary_key=True)
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.generate_key()
        return super().save(*args, **kwargs)

    def generate_key(self):
        return binascii.hexlify(os.urandom(20)).decode()


class ClienteTokenAuthentication(TokenAuthentication):
    keyword = "Bearer"

    def authenticate_credentials(self, key):
        try:
            token_obj = ClienteToken.objects.get(key=key)
        except ClienteToken.DoesNotExist:
            raise AuthenticationFailed("Invalid token.")

        if not token_obj.cliente.is_authenticated():
            raise AuthenticationFailed("User inactive or deleted.")

        return (token_obj.cliente, token_obj)
