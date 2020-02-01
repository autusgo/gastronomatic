# Generated by Django 3.0.2 on 2020-01-30 14:42

from django.db import migrations, models
import django.db.models.deletion
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0018_factura_producto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='factura',
            name='producto',
        ),
        migrations.AddField(
            model_name='factura',
            name='detalle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='compras.Detalle'),
        ),
        migrations.AlterField(
            model_name='factura',
            name='fecha_de_pago',
            field=model_utils.fields.MonitorField(blank=True, default=None, monitor='estado', null=True, verbose_name='Fecha de pago', when={'Pago'}),
        ),
    ]