# Generated by Django 4.2.2 on 2023-06-20 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sneakerApp', '0007_zapatilla_imagen_muestra_zapatilla_imagen_muestra_2'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name': 'Categoría', 'verbose_name_plural': 'Categorías'},
        ),
        migrations.AlterModelOptions(
            name='tallaeur',
            options={'verbose_name': 'Talla EUR', 'verbose_name_plural': 'Tallas EUR'},
        ),
    ]
