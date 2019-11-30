from django import forms
from .models import Producto

class Formulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    mensaje = forms.CharField()
    mail = forms.EmailField()


class ProdForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('codigoProducto','nombreProducto', 'descripcion','stock','precio','imagen')
