# Generated by Django 4.1.4 on 2023-06-26 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreApp', '0005_alter_contactanos_mensaje'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactanos',
            name='propuesta',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]