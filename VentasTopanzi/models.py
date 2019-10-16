from django.db import models
# Clase cliente, Productos, Contacto, Compra
# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField('Nombre', max_length=30)
    apellido = models.CharField('Apellido', max_length=30)
    correo = models.EmailField('Correo')
    telefono = models.CharField('Teléfono', max_length=20)
    rut = models.IntegerField('Rut sin DV: 18224351', max_length=20).primary_key
    dv = models.CharField('Dígito Verificador', max_length=1)

    def boleta(self):
        return "Nombre: " + self.nombre + "\n Apellido: " + self.apellido + "\n Correo: " + self.correo + "\n Rut: "+ self.rut + "-" + self.dv


class Producto(models.Model):
    codigoProducto = models.CharField('Código Producto', max_length=30)
    nombreProducto = models.CharField('Nombre Producto', max_length=30)
    descripcion = models.TextField('Descripción del producto', max_length=500)
    stock = models.IntegerField('Stock', max_length=20).primary_key

    

class Venta(models.Model):
    nombre = models.CharField('Nombre', max_length=30)
    apellido = models.CharField('Apellido', max_length=30)
    correo = models.EmailField('Correo')
    telefono = models.CharField('Teléfono', max_length=20)
    rut = models.IntegerField('Rut sin DV: 18224351', max_length=20).primary_key
    dv = models.CharField('Dígito Verificador', max_length=1)

class Contacto(models.Model):
    nombre = models.CharField('Nombre', max_length=30)
    apellido = models.CharField('Apellido', max_length=30)
    correo = models.EmailField('Correo')
    telefono = models.CharField('Teléfono', max_length=20)
    rut = models.IntegerField('Rut sin DV: 18224351', max_length=20).primary_key
    dv = models.CharField('Dígito Verificador', max_length=1)