from django.utils import timezone
# from .models import Post
from django.shortcuts import render, get_object_or_404 
from django.shortcuts import redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect 
from django.urls import reverse_lazy, reverse
from .forms import FormularioForm
from .forms import ProdForm
from .models import Producto
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from apps.VentasTopanzi.quickstart.serializers import UserSerializer, GroupSerializer
# Create your views here.

def index (request):
    return render(request, 'VentasTopanzi/index.html')

def Nosotros (request):
    return render(request, 'VentasTopanzi/Nosotros.html')

def Productos (request):
    prod = Producto.objects.order_by('codigoProducto')
    return render(request, 'VentasTopanzi/Productos.html', {'prod': prod })

def Contacto (request):
    if request.method == 'POST':
        form = FormularioForm(request.POST, request.FILES)
        if form.is_valid():
            cont = form.save(commit=False)
            cont.save()
            prod = Producto.objects.order_by('codigoProducto')
            return render(request, 'VentasTopanzi/Productos.html', {'prod': prod })
    else:
        form = FormularioForm()
    return render(request, 'VentasTopanzi/Contacto.html', {'form': form})

def prod_new(request):
    if request.method == "POST":
        form = ProdForm(request.POST, request.FILES)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.save()
            return redirect('prod_detail', pk=prod.pk)
    else:
        form = ProdForm()
    return render(request, 'VentasTopanzi/prod_new.html', {'form': form})

def Galeria (request):
    return render(request, 'VentasTopanzi/Galeria.html')

def prod_detail(request, pk):
    prod = get_object_or_404(Producto, pk=pk)
    return render(request, 'VentasTopanzi/prod_detail.html', {'prod': prod})





def prod_edit(request, pk):
    prod = get_object_or_404(Producto, pk=pk)
    if request.method == "POST":
        form = ProdForm(request.POST, instance=prod)
        if form.is_valid():
            prod = form.save(commit=False)
            prod.save()
            return redirect('prod_detail', pk=prod.pk)
    else:
        form = ProdForm(instance=prod)
    return render(request, 'VentasTopanzi/prod_edit.html', {'form': form})

def prod_delete(request, pk):
    pro = get_object_or_404(Producto, pk=pk)
    pro.delete()
    prod = Producto.objects.order_by('codigoProducto')
    return render(request, 'VentasTopanzi/Productos.html', {'prod': prod })

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
