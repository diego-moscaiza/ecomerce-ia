# Generated by Django 5.0.6 on 2024-07-30 15:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrega_productos', '0001_initial'),
        ('productos', '0021_alter_producto_id_estante'),
        ('proveedor', '0003_alter_proveedor_correo_alter_proveedor_direccion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrega',
            name='id_producto',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='productos.producto'),
        ),
        migrations.AlterField(
            model_name='entrega',
            name='id_proveedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='proveedor.proveedor'),
        ),
    ]