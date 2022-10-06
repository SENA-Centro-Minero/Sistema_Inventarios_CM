from django.forms import ModelForm
from usuarios.models import  Usuario


class UsuarioForm(ModelForm):
    class Meta:
        model= Usuario
        exclude=['estado']
