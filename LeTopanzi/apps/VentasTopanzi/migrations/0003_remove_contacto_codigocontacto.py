# Generated by Django 2.2.6 on 2019-12-02 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('VentasTopanzi', '0002_auto_20191130_1624'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacto',
            name='codigoContacto',
        ),
    ]
