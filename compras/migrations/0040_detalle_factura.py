# Generated by Django 3.0.2 on 2020-02-02 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0039_auto_20200202_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='detalle',
            name='factura',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='compras.Factura'),
        ),
    ]