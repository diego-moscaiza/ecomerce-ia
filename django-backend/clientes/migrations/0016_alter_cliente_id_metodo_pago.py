# Generated by Django 5.0.6 on 2024-05-31 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0015_alter_cliente_id_metodo_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='id_metodo_pago',
            field=models.IntegerField(blank=True, default='', null=True),
        ),
    ]
