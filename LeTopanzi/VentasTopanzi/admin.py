from django.contrib import admin
from .models import Cliente
from .models import Producto
from .models import Venta
from .models import Contacto

# Register your models here.


admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Venta)
admin.site.register(Contacto)