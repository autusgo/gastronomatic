# Generated by Django 3.0.2 on 2020-02-01 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0030_detalle_subtotal'),
    ]

    operations = [
        migrations.AddField(
            model_name='factura',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True),
        ),
    ]