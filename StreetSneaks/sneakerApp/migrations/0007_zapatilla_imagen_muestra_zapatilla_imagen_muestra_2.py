# Generated by Django 4.1.4 on 2023-05-31 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sneakerApp', '0006_zapatilla_id_prod'),
    ]

    operations = [
        migrations.AddField(
            model_name='zapatilla',
            name='imagen_muestra',
            field=models.ImageField(blank=True, default='null', upload_to='imagen', verbose_name='Imagen muestra'),
        ),
        migrations.AddField(
            model_name='zapatilla',
            name='imagen_muestra_2',
            field=models.ImageField(blank=True, default='null', upload_to='imagen', verbose_name='Imagen muestra'),
        ),
    ]