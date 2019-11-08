from django.shortcuts import render
from .models import Producto

# Create your views here.
def index (request):
    return render(request, 'VentasTopanzi/index.html', {})

def Nosotros (request):
    return render(request, 'VentasTopanzi/Nosotros.html', {})

def Productos (request):
    prod = Producto.objects.order_by('nombreProducto')
    return render(request, 'VentasTopanzi/Productos.html', {'prod': prod })

def Contacto (request):
    return render(request, 'VentasTopanzi/Contacto.html', {})

def Galeria (request):
    return render(request, 'VentasTopanzi/Galeria.html', {})