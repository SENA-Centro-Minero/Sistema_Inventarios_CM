from django.forms import ModelForm, widgets
from usuarios.models import  Usuario, Departamento, Municipio,Empresa


class UsuarioForm(ModelForm):
    class Meta:
        model= Usuario
        exclude=['estado','user']
        widgets={
            'fecha_nacimiento': widgets.DateInput(attrs={'type':'date'})
        }
class EmpresaForm(ModelForm):
    class Meta:
        model= Empresa
        exclude=['estado']
class EmpresaUpdateForm(ModelForm):
    class Meta:
        model= Empresa
        exclude=['estado','nit']
class DepartamentoForm(ModelForm):
    class Meta:
        model= Departamento
        exclude=['estado']
class MunicipioForm(ModelForm):
    class Meta:
        model= Municipio
        exclude=['estado']