# Generated by Django 5.0.6 on 2024-06-24 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0020_clientetoken_created_at'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ClienteToken',
        ),
    ]