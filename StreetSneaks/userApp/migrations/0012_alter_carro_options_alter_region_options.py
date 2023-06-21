

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0011_alter_carro_direccion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carro',
            options={'verbose_name': 'Carro', 'verbose_name_plural': 'Carros'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'verbose_name': 'Región', 'verbose_name_plural': 'Regiones'},
        ),
    ]
