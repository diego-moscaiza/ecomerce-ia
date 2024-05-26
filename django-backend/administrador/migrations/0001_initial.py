# Generated by Django 5.0.6 on 2024-05-26 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id_administrador', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=40, null=True)),
                ('apellido', models.CharField(max_length=60, null=True)),
                ('documento', models.CharField(max_length=11, null=True)),
                ('telefono', models.CharField(max_length=9, null=True)),
                ('usuario', models.CharField(max_length=50, null=True)),
                ('correo', models.CharField(max_length=30, null=True)),
                ('contraseña', models.CharField(max_length=128, null=True)),
            ],
        ),
    ]
