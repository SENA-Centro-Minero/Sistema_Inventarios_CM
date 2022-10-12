from django.forms import ModelForm
from usuarios.models import  Usuario, Departamento, Municipio,Empresa


class UsuarioForm(ModelForm):
    class Meta:
        model= Usuario
        exclude=['estado']
class EmpresaForm(ModelForm):
    class Meta:
        model= Empresa
        exclude=['estado']
class DepartamentoForm(ModelForm):
    class Meta:
        model= Departamento
        exclude=['estado']
class MunicipioForm(ModelForm):
    class Meta:
        model= Municipio
        exclude=['estado']