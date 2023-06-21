# Generated by Django 4.1.4 on 2023-06-20 19:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ventaApp', '0005_alter_cupon_options_alter_iva_options_boleta'),
    ]

    operations = [
        migrations.AddField(
            model_name='boleta',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]