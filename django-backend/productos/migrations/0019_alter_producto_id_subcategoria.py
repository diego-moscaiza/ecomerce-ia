# Generated by Django 5.0.6 on 2024-07-29 22:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0005_subcategoria'),
        ('productos', '0018_alter_producto_id_estante_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id_subcategoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categoria.subcategoria'),
        ),
    ]
