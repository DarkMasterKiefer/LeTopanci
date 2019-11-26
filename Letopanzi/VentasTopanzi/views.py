from django.shortcuts import render
from .models import Producto
from django.shortcuts import render, get_object_or_404

# Create your views here.
def index (request):
    return render(request, 'VentasTopanzi/index.html', {})

def Nosotros (request):
    return render(request, 'VentasTopanzi/Nosotros.html', {})

def Productos (request):
    prod = Producto.objects.order_by('codigoProducto')
    return render(request, 'VentasTopanzi/Productos.html', {'prod': prod })

def Contacto (request):
    return render(request, 'VentasTopanzi/Contacto.html', {})

def Galeria (request):
    return render(request, 'VentasTopanzi/Galeria.html', {})

def prod_detail(request, pk):
    prod = get_object_or_404(Producto, pk=pk)
    return render(request, 'VentasTopanzi/prod_detail.html', {'prod': prod})
