# Generated by Django 4.1.4 on 2023-06-07 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventaApp', '0003_alter_cupon_valor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Iva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField(null=True, verbose_name='Valor')),
            ],
        ),
    ]
