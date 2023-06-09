# Generated by Django 4.1.4 on 2023-06-29 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventaApp', '0016_alter_venta_options_boleta_estado_envio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=255, verbose_name='Nombre del estado')),
                ('valor', models.IntegerField(null=True, verbose_name='Porcentaje del recorrido')),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
            },
        ),
    ]
