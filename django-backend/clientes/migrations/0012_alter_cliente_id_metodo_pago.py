# Generated by Django 5.0.6 on 2024-05-27 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0011_alter_cliente_fecha_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='id_metodo_pago',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]