from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password, check_password


class Cliente(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=40, blank=True)
    apellido = models.CharField(max_length=60, blank=True)
    documento = models.CharField(max_length=11, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    sexo = models.CharField(max_length=10, blank=True)
    telefono = models.CharField(max_length=9, blank=True)
    id_metodo_pago = models.IntegerField(null=True, blank=True)
    correo = models.CharField(max_length=30)
    contraseña = models.CharField(max_length=128)

    def set_password(self, raw_password):
        self.contraseña = make_password(raw_password)
        self._contraseña = raw_password

    def is_authenticated(self):
        return True

    def check_password(self, raw_password):
        """
        Return a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """

        def setter(raw_password):
            self.set_password(raw_password)
            # Password hash upgrades shouldn't be considered password changes.
            self._password = None
            self.save(update_fields=["contraseña"])

        return check_password(raw_password, self.contraseña, setter)
