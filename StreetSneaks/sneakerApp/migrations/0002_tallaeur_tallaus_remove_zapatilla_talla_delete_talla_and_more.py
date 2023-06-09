# Generated by Django 4.1.4 on 2023-05-28 20:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sneakerApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TallaEUR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(default='null', max_length=50, null=True, verbose_name='Tipo EUR')),
                ('number', models.IntegerField(null=True, verbose_name='Número de talla')),
            ],
        ),
        migrations.CreateModel(
            name='TallaUS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(default='null', max_length=50, null=True, verbose_name='Tipo US')),
                ('number', models.IntegerField(null=True, verbose_name='Número de talla')),
            ],
        ),
        migrations.RemoveField(
            model_name='zapatilla',
            name='talla',
        ),
        migrations.DeleteModel(
            name='Talla',
        ),
        migrations.AddField(
            model_name='zapatilla',
            name='tallaEUR',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sneakerApp.tallaeur', verbose_name='Talla EUR'),
        ),
        migrations.AddField(
            model_name='zapatilla',
            name='tallaUS',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sneakerApp.tallaus', verbose_name='Talla US'),
        ),
    ]
