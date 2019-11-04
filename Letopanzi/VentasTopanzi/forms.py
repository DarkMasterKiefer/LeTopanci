from django import forms
from .models import Cliente
from .models import Producto
from .models import Venta
from .models import Contacto

class ProdForm(forms.ModelForm):

    class Meta:
        model = Producto
        fields = ('codigoProducto', 'nombreProducto', 'descripcion', 'stock', 'precio', 'imagen')
