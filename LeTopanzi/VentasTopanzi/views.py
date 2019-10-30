from django.shortcuts import render
from django.utils import timezone
# from .models import Post
from django.shortcuts import render, get_object_or_404 
# from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.
def index (request):
    return render(request, 'VentasTopanzi/index.html')

def Nosotros (request):
    return render(request, 'VentasTopanzi/Nosotros.html')

def Productos (request):
    return render(request, 'VentasTopanzi/Productos.html')

def Contacto (request):
    return render(request, 'VentasTopanzi/Contacto.html')

def Galeria (request):
    return render(request, 'VentasTopanzi/Galeria.html')