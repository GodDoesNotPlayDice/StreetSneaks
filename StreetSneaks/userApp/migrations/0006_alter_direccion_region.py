# Generated by Django 4.1.4 on 2023-06-01 02:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0005_direccion_region'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direccion',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userApp.region', verbose_name='Region'),
        ),
    ]
