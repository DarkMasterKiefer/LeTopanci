from django import forms
from .models import Producto

class ProdForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('codigoProducto','nombreProducto', 'descripcion','stock','precio','imagen')
