# Generated by Django 4.1.4 on 2023-05-30 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sneakerApp', '0005_alter_zapatilla_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='zapatilla',
            name='id_prod',
            field=models.CharField(max_length=50, null=True, unique=True, verbose_name='ID'),
        ),
    ]
