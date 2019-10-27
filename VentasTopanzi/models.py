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
    direccion = models.CharField('Dirección',max_length=120)

    def boleta(self):
        return "Nombre: " + self.nombre + "\n Apellido: " + self.apellido + "\n Correo: " + self.correo + "\n Rut: "+ self.rut + "-" + self.dv + "\n Dirección: "+self.direccion


class Producto(models.Model):
    codigoProducto = models.CharField('Código Producto', max_length=30).primary_key
    nombreProducto = models.CharField('Nombre Producto', max_length=30)
    descripcion = models.TextField('Descripción del producto', max_length=500)
    stock = models.IntegerField('Stock', max_length=20)
    precio = models.IntegerField('Precio', max_length=20)
    imagen = models.ImageField(upload_to='None')

    def boletaProd(self):
        return "Nombre Producto: " +self.nombreProducto + "\n Precio: "+self.precio 

    

class Venta(models.Model):
    codigoVenta = models.CharField('Código Producto', max_length=30).primary_key
    precioVenta = models.IntegerField('Precio', max_length=20)
    descripcionVenta = models.TextField('Descripción del producto', max_length=500)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

class Contacto(models.Model):
    codigoContacto = models.CharField('Código Contacto', max_length=30).primary_key
    nombre = models.CharField('Nombre', max_length=30)
    apellido = models.CharField('Apellido', max_length=30)
    correo = models.EmailField('Correo')
    telefono = models.CharField('Teléfono', max_length=20)
    mensaje = models.TextField('Ingrese el mensaje', max_length=500)


