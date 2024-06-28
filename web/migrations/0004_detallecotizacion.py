# Generated by Django 5.0.6 on 2024-06-26 09:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_preciounitario'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleCotizacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('sub_total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('cotizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.cotizacion')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.producto')),
            ],
        ),
    ]