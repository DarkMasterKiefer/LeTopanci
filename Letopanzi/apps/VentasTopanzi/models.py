from django.db import models
from django.conf import settings
# Clase cliente, Productos, Contacto, Compra
# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField('Nombre', max_length=30)
    apellido = models.CharField('Apellido', max_length=30)
    correo = models.EmailField('Correo')
    telefono = models.CharField('Teléfono', max_length=20)
    rut = models.IntegerField('Rut sin DV: 18224351')
    dv = models.CharField('Dígito Verificador', max_length=1)
    direccion = models.CharField('Dirección',max_length=120)

    def boleta(self):
        return "Nombre: " + self.nombre + "\n Apellido: " + self.apellido + "\n Correo: " + self.correo + "\n Rut: "+ self.rut + "-" + self.dv + "\n Dirección: "+self.direccion


class Producto(models.Model):
    codigoProducto = models.CharField('Código Producto', max_length=30)
    nombreProducto = models.CharField('Nombre Producto', max_length=30)
    descripcion = models.TextField('Descripción del producto', max_length=500)
    stock = models.IntegerField('Stock')
    precio = models.IntegerField('Precio')
    imagen =models.ImageField(blank=True, null=True)

    def boletaProd(self):
        return "Nombre Producto: " +self.nombreProducto + "\n Precio: "+self.precio 

    def publish(self):
        self.save()

    def __str__(self):
        return self.nombreProducto
    

class Venta(models.Model):
    codigoVenta = models.CharField('Código Producto', max_length=30)
    precioVenta = models.IntegerField('Precio')
    descripcionVenta = models.TextField('Descripción del producto', max_length=500)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Contacto(models.Model):
    nombre = models.CharField('Nombre', max_length=30)
    apellido = models.CharField('Apellido', max_length=30)
    correo = models.EmailField('Correo')
    telefono = models.CharField('Teléfono', max_length=20)
    mensaje = models.TextField('Ingrese el mensaje', max_length=500)

    def publish(self):
        self.save()

    def __str__(self):
        return self.mensaje
