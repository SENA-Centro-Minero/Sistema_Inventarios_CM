from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator


class Sucursal(models.Model):
    nombre=models.TextField(max_length=80, verbose_name="Nombre Sucursal")
    #empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name="Empresa")
    direccion=models.CharField(max_length=70, verbose_name="Dirección")
    telefono=models.CharField(max_length=20, verbose_name="Teléfono", blank=True)
    #administrador=models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Administrador")
    #municipio=models.ForeignKey(Municipio, on_delete=models.CASCADE, verbose_name="Municipio")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

# Create your models here.
class Factura(models.Model):
    fecha=models.DateField(verbose_name="Fecha Factura", help_text=u"MM/DD/AAAA")
