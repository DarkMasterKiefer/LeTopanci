from django.shortcuts import render
from django.utils import timezone
from .models import Cliente
from .models import Producto
from .models import Venta
from .models import Contacto
from django.shortcuts import render, get_object_or_404 
# from .forms import PostForm
from django.shortcuts import redirect
from .forms import ProdForm

# Create your views here.
def index (request):
    return render(request, 'VentasTopanzi/index.html')

def Nosotros (request):
    return render(request, 'VentasTopanzi/Nosotros.html')

def Productos (request):
    prod = Producto.objects.order_by('nombreProducto')
    return render(request, 'VentasTopanzi/Productos.html',{'prod',prod} )

def Contactos (request):
    return render(request, 'VentasTopanzi/Contacto.html')

def Galeria (request):
    return render(request, 'VentasTopanzi/Galeria.html')

def prod_new(request):
    if request.method == "PRODUCTO":
        form = ProdForm(request.PRODUCTO)
    if form.is_valid():
        prod = form.save(commit=True)
        prod.save()
        return redirect('prod_detail', pk=prod.pk)
    else:
        form = ProdForm()
    return render(request, 'VentasTopanzi/prod_edit.html', {'form': form})


def prod_detail(request, pk):
    prod = get_object_or_404(Producto, pk=pk)
    return render(request, 'VentasTopanzi/prod_detail.html', {'prod': prod})
