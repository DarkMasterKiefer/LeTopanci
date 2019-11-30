from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            
        ]
        labels = {
            'username': 'Nombre se Usuario',
            'email': 'Correo',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            
        }