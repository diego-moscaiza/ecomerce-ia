# Generated by Django 5.0.6 on 2024-06-03 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0016_alter_cliente_id_metodo_pago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
    ]