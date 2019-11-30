from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from apps.usuario.forms import RegistroForm
from django.contrib.auth import login, logout
from django.shortcuts import HttpResponseRedirect

# Create your views here.

class RegistroUsuario(CreateView):
    model = User
    template_name = "usuario/registrar.html"
    form_class = RegistroForm
    success_url = reverse_lazy('index')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/VentasTopanzi/Nosotros")