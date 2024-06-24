from django.db import models
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
        self.password = make_password(raw_password)
        self._password = raw_password

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def is_authenticated(self):
        return True
