# Generated by Django 4.1.4 on 2023-06-21 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventaApp', '0014_boleta_fecha_actual'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boleta',
            name='fecha',
            field=models.CharField(max_length=255, verbose_name='Fecha Entrega'),
        ),
    ]
