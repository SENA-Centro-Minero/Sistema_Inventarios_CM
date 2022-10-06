
from django.utils.translation import gettext_lazy as _
from django.db import models

# Create your models here.

class Empresa(models.Model):
    nombre=models.TextField(max_length=80, verbose_name="Nombre Empresa")
    nit=models.TextField(max_length=20, verbose_name="NIT Empresa")
    class Estado(models.Model):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

class Departamento(models.Model):
    nombre=models.TextField(max_length=90, verbose_name="Nombre Departamento")
    class Estado(models.Model):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

class Municipio(models.Model):
    nombre=models.TextField(max_length=90, verbose_name="Nombre Municipio")
    departamento=models.ForeignKey(Departamento, on_delete=models.CASCADE, verbose_name="Departamento")
    class Estado(models.Model):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

class Sucursal(models.Model):
    nombre=models.TextField(max_length=80, verbose_name="Nombre Sucursal")
    empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name="Empresa")
    direccion=models.CharField(max_length=70, verbose_name="Dirección")
    telefono=models.CharField(max_length=20, verbose_name="Teléfono", blank=True)
    administrador=models.ForeignKey("Usuario", on_delete=models.CASCADE, verbose_name="Administrador")
    municipio=models.ForeignKey(Municipio, on_delete=models.CASCADE, verbose_name="Municipio")
    class Estado(models.Model):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

class Usuario(models.Model):
    nombres=models.CharField(max_length=60, verbose_name="Nombres")
    apellidos=models.CharField(max_length=60, verbose_name="Apellidos")
    class TipoDocumento(models.Model):
        CC='C.C', _('Cédula de Ciudadanía')
        CE='C.E', _('Cédula de Extranjería')
        TI='T.I', _('Tarjeta de Identidad')
        OT='Otro', _('Otro Tipo de Documento')
    tipoDocumento=models.CharField(max_length=4, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de Documento")
    documento=models.CharField(max_length=50, verbose_name="Número de Documento")
    telefono=models.CharField(max_length=20, verbose_name="Teléfono")
    direccion=models.CharField(max_length=70, verbose_name="Dirección")
    municipio=models.ForeignKey(Municipio, on_delete=models.CASCADE, verbose_name="Municipio")
    fecha_nacimiento=models.DateField(verbose_name="Fecha de Nacimiento", help_text=u"MM/DD/AAAA")
    class Rol(models.Model):
        Administrador='Administrador', _('Administrador')
        Empleado='Empleado', _('Empleado')
        Cliente='Cliente', _('Cliente')
        Proveedor='Proveedor', _('Proveedor')
    rol=models.CharField(max_length=13, choices=Rol.choices, default=Rol.Empleado, verbose_name="Rol")
    sucursal=models.ForeignKey("Sucursal", on_delete=models.CASCADE, verbose_name="Sucursal")
    class Estado(models.Model):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

