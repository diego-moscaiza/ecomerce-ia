# Generated by Django 5.0.6 on 2024-05-27 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0007_alter_cliente_fecha_nacimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(null=True),
        ),
    ]
