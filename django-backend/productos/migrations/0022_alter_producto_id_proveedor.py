# Generated by Django 5.0.6 on 2024-07-30 15:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0021_alter_producto_id_estante'),
        ('proveedor', '0003_alter_proveedor_correo_alter_proveedor_direccion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id_proveedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='proveedor.proveedor'),
        ),
    ]