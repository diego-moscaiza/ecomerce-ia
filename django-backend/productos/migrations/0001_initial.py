# Generated by Django 5.0.6 on 2024-05-25 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, null=True)),
                ('descripcion', models.CharField(max_length=100, null=True)),
                ('cantidad', models.IntegerField(null=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('estado', models.CharField(max_length=1, null=True)),
            ],
        ),
    ]