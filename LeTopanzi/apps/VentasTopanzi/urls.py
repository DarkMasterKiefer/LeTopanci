from django.urls import include, path
from django.conf.urls import url, include
from apps.VentasTopanzi.quickstart import views
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    
    path('', views.index, name='index'),
    path('VentasTopanzi/Nosotros', views.Nosotros, name='Nosotros'),
    path('VentasTopanzi/Productos', views.Productos, name='Productos'),
    path('VentasTopanzi/Contacto', views.Contacto, name='Contacto'),
    path('VentasTopanzi/Galeria', views.Galeria, name='Galeria'),
    path('VentasTopanzi/login', views.Galeria, name='Login'),
    path('prod/<int:pk>/', views.prod_detail, name='prod_detail'),
    path('prod/new', views.prod_new, name='prod_new'),
    path('prod/<int:pk>/edit/', views.prod_edit, name='prod_edit'),
    path('prod/<int:pk>/delete/', views.prod_delete, name='prod_delete'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]