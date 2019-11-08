# Generated by Django 2.2.6 on 2019-11-08 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=30, verbose_name='Apellido')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo')),
                ('telefono', models.CharField(max_length=20, verbose_name='Teléfono')),
                ('dv', models.CharField(max_length=1, verbose_name='Dígito Verificador')),
                ('direccion', models.CharField(max_length=120, verbose_name='Dirección')),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=30, verbose_name='Apellido')),
                ('correo', models.EmailField(max_length=254, verbose_name='Correo')),
                ('telefono', models.CharField(max_length=20, verbose_name='Teléfono')),
                ('mensaje', models.TextField(max_length=500, verbose_name='Ingrese el mensaje')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreProducto', models.CharField(max_length=30, verbose_name='Nombre Producto')),
                ('descripcion', models.TextField(max_length=500, verbose_name='Descripción del producto')),
                ('stock', models.IntegerField(verbose_name='Stock')),
                ('precio', models.IntegerField(verbose_name='Precio')),
                ('imagen', models.ImageField(upload_to='None')),
            ],
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precioVenta', models.IntegerField(verbose_name='Precio')),
                ('descripcionVenta', models.TextField(max_length=500, verbose_name='Descripción del producto')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VentasTopanzi.Cliente')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VentasTopanzi.Producto')),
            ],
        ),
    ]
