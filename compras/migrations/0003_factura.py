# Generated by Django 3.0.2 on 2020-01-21 23:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('compras', '0002_auto_20200120_2035'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=0, max_digits=5)),
                ('monto', models.DecimalField(decimal_places=2, max_digits=9)),
                ('estado', models.CharField(max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compras.Producto')),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compras.Proveedor')),
            ],
            options={
                'verbose_name_plural': 'Facturas',
            },
        ),
    ]