# Generated by Django 5.0.6 on 2024-05-27 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_alter_producto_cantidad_alter_producto_estado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]