from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator

# Create your models here.

class Producto(models.Model):
    nombre=models.CharField(max_length=60, verbose_name="Nombre Producto")
    precio=models.PositiveBigIntegerField(validators=[MinValueValidator(1)], verbose_name="Precio")
    porcentaje_ganancia=models.DecimalField(validators=[MinValueValidator(0.0)],decimal_places=1,max_digits=2, verbose_name="Porcentaje Ganancia")
    stock= models.PositiveIntegerField(validators=[MinValueValidator(0)], verbose_name="Stock")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    def __str__(self):
        return "%s | %s"%(self.nombre,self.stock)
class Categoria(models.Model):
    nombre=models.TextField(max_length=80, verbose_name="Nombre Categoria")
    descripcion=models.TextField(max_length=200, verbose_name="Descripción")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    created_at=models.DateField(verbose_name="Fecha de creación", help_text=u"MM/DD/AAAA")
    updated_at=models.DateField(verbose_name="Fecha de actualización", help_text=u"MM/DD/AAAA")

class Producto_Categoria(models.Model):
    codigo_producto=models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Código Producto")
    codigo_categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Código Categoría")

