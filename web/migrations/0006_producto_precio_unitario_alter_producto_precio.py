# Generated by Django 5.0.6 on 2024-06-27 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_producto_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='precio_unitario',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
    ]
