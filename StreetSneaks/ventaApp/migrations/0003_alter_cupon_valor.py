# Generated by Django 4.1.4 on 2023-06-03 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventaApp', '0002_rename_cupones_cupon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cupon',
            name='valor',
            field=models.IntegerField(null=True, verbose_name='Valor'),
        ),
    ]
