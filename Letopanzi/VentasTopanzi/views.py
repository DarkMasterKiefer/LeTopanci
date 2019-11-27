from django.shortcuts import render
from .models import Producto
from django.shortcuts import render, get_object_or_404
from .forms import ProdForm
from django.shortcuts import redirect

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

def prod_new(request):
    if request.method == "PRODUCTO":
        form = ProdForm(request.PRODUCTO)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.save()
            return redirect('prod_detail', pk=prod.pk)
    else:
        form = ProdForm()
    return render(request, 'VentasTopanzi/prod_new.html', {'form': form})

def prod_edit(request, pk):
    prod = get_object_or_404(Producto, pk=pk)
    if request.method == "PRODUCTO":
        form = ProdForm(request.PRODUCTO, instance=prod)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.save()
            return redirect('prod_detail', pk=prod.pk)
    else:
        form = ProdForm(instance=prod)
    return render(request, 'VentasTopanzi/prod_edit.html', {'form': form})