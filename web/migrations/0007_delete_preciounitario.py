# Generated by Django 5.0.6 on 2024-06-28 00:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_producto_precio_unitario_alter_producto_precio'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PrecioUnitario',
        ),
    ]