from django.forms import ModelForm, widgets
from django_select2 import forms as s2forms
from productos.models import Producto
from django_select2 import forms as s2forms

from facturas.models import Factura, FacturaDetalleCompra, FacturaDetalleVenta

class ProductoWidget(s2forms.ModelSelect2Widget):
    search_fields ={
        "nombre__icontains",
        "id__icontains"
    }

class FacturaForm(ModelForm):
    class Meta:
        model= Factura
        exclude=['estado','empleado','monto']
        widgets={
            'fecha': widgets.DateInput(attrs={'type':'date'}, format='%Y-%m-%d')
        }

class FacturaDetalleCompraForm(ModelForm):
    class Meta:
        model= FacturaDetalleCompra
        exclude=['estado','factura']
        widgets={
            'producto':ProductoWidget,
            'fechaExpiracion': widgets.DateInput(attrs={'type':'date'}, format='%Y-%m-%d')

        }


class FacturaDetalleVentaForm(ModelForm):
    class Meta:
        model= FacturaDetalleVenta
        fields='__all__'
        widgets={
            'producto':ProductoWidget
        }