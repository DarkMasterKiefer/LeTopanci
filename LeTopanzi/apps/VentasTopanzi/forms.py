from django import forms
from .models import Producto, Contacto

class FormularioForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ('nombre', 'apellido','correo','telefono','mensaje')
        



class ProdForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('codigoProducto','nombreProducto', 'descripcion','stock','precio','imagen')
