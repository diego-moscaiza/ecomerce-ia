# Generated by Django 5.0.6 on 2024-05-27 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventario',
            old_name='ubicacion',
            new_name='numero_almacen',
        ),
        migrations.RemoveField(
            model_name='inventario',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='inventario',
            name='stock',
        ),
    ]