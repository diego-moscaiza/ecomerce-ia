# Generated by Django 5.0.6 on 2024-06-09 02:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0004_alter_categoria_descripcion'),
        ('productos', '0008_remove_producto_id_categoria_producto_genero_and_more'),
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='id_categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categoria.categoria'),
        ),
        migrations.AddField(
            model_name='producto',
            name='id_subcategoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categoria.subcategoria'),
        ),
    ]
