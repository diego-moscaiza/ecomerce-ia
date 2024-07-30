# Generated by Django 5.0.6 on 2024-07-29 22:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0005_subcategoria'),
        ('productos', '0019_alter_producto_id_subcategoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='id_subcategoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='categoria.subcategoria'),
        ),
    ]