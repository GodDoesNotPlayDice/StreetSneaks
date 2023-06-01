# Generated by Django 4.1.4 on 2023-06-01 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sneakerApp', '0007_zapatilla_imagen_muestra_zapatilla_imagen_muestra_2'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userApp', '0006_alter_direccion_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sneakerApp.zapatilla')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
