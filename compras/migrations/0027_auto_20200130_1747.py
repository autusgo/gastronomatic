# Generated by Django 3.0.2 on 2020-01-30 20:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0026_auto_20200130_1746'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detalle',
            old_name='nombre',
            new_name='producto',
        ),
    ]