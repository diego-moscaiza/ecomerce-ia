# Generated by Django 5.0.6 on 2024-06-08 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0007_producto_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='id_categoria',
        ),
        migrations.AddField(
            model_name='producto',
            name='genero',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='marca',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='talla',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]