from django.urls import include, path
from . import views
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.index, name='index'),
    path('VentasTopanzi/Nosotros', views.Nosotros, name='Nosotros'),
    path('VentasTopanzi/Productos', views.Productos, name='Productos'),
    path('VentasTopanzi/Contactos', views.Contacto, name='Contacto'),
    path('VentasTopanzi/Galeria', views.Galeria, name='Galeria'),
    path('prod/<int:pk>/', views.prod_detail, name='prod_detail'),
    path('prod/new', views.prod_new, name='prod_new'),
]