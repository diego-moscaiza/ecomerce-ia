# Generated by Django 5.0.6 on 2024-06-09 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0012_alter_producto_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='img',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
