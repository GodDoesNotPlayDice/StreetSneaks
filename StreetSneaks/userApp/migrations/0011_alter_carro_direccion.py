# Generated by Django 4.1.4 on 2023-06-06 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0010_alter_carro_direccion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carro',
            name='direccion',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userApp.direccion'),
        ),
    ]
