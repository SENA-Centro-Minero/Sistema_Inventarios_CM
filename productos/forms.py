from django.forms import ModelForm
from productos.models import  Producto
class ProductoForm(ModelForm):
    class Meta:
        model= Producto
        exclude=['estado']