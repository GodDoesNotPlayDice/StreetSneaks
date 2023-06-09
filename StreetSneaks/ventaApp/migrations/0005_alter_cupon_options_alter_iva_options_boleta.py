from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0012_alter_carro_options_alter_region_options'),
        ('ventaApp', '0004_iva'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cupon',
            options={'verbose_name': 'Cupon', 'verbose_name_plural': 'Cupones'},
        ),
        migrations.AlterModelOptions(
            name='iva',
            options={'verbose_name': 'Iva', 'verbose_name_plural': 'Ivas'},
        ),
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_boleta', models.CharField(max_length=255, verbose_name='Id Boleta')),
                ('fecha', models.DateField(auto_now_add=True, verbose_name='Fecha')),
                ('total', models.IntegerField(null=True, verbose_name='Total')),
                ('cupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventaApp.cupon', verbose_name='Cupon')),
                ('iva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventaApp.iva', verbose_name='Iva')),
                ('productos', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userApp.carro', verbose_name='Productos')),
            ],
            options={
                'verbose_name': 'Boleta',
                'verbose_name_plural': 'Boletas',
            },
        ),
    ]
