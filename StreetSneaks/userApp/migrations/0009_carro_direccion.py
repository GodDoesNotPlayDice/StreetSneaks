# Generated by Django 4.1.4 on 2023-06-06 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0008_carro_cupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='carro',
            name='direccion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userApp.direccion'),
        ),
    ]