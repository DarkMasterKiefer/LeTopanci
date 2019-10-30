from django.urls import include, path
from . import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('VentasTopanzi/Nosotros', views.Nosotros, name='Nosotros'),
    path('VentasTopanzi/Productos', views.Productos, name='Productos'),
    path('VentasTopanzi/Contactos', views.Contacto, name='Contacto'),
    path('VentasTopanzi/Galeria', views.Galeria, name='Galeria'),
]