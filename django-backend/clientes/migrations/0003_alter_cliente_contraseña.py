# Generated by Django 5.0.6 on 2024-05-19 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0002_alter_cliente_contraseña_alter_cliente_correo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='contraseña',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
