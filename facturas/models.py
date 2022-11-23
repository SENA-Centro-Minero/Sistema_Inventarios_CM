
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from productos.models import Producto
from usuarios.models import Usuario



# Create your models here.
class Factura(models.Model):
    numeroSerie=models.IntegerField(primary_key=True,verbose_name="Número de Serie",unique=True)
    monto=models.BigIntegerField(validators=[MinValueValidator(0)],default=0, verbose_name="Monto")
    fecha=models.DateField(auto_now=True,verbose_name="Fecha Factura")
    class TipoFactura(models.TextChoices):
        VENTA='Venta', _('Venta')
        COMPRA='Compra', _('Compra')
    tipoFactura=models.CharField(max_length=6, choices=TipoFactura.choices, default=TipoFactura.VENTA, verbose_name="Tipo de Factura")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    cliente=models.ForeignKey(Usuario,verbose_name="Cliente",on_delete=models.CASCADE,related_name='Cliente')
    empleado=models.ForeignKey(Usuario,  verbose_name="Empleado",on_delete=models.CASCADE,related_name='Empleado')
    def __str__(self):
        return self.numeroSerie

class FacturaDetalleCompra(models.Model):
    factura=models.ForeignKey(Factura, on_delete=models.CASCADE, verbose_name="Número Factura")
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Producto")
    lote=models.IntegerField(validators=[MinValueValidator(0)], verbose_name="Lote")
    fechaExpiracion=models.DateField(verbose_name="Fecha Expiración")
    cantidad=models.IntegerField(validators=[MinValueValidator(0)], verbose_name="Cantidad")
    precio=models.BigIntegerField(validators=[MinValueValidator(0)], verbose_name="Precio")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    @property
    def subtotal(self):
        return self.precio*self.cantidad

class FacturaDetalleVenta(models.Model):
    cantidad=models.IntegerField(validators=[MinValueValidator(0)], verbose_name="Cantidad")
    precio=models.BigIntegerField(validators=[MinValueValidator(0)], verbose_name="Precio")
    factura=models.ForeignKey(Factura, on_delete=models.CASCADE, verbose_name="Número Factura")
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Detalle Factura")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

class Devolucion(models.Model):
    fechaDevolucion=models.DateField(auto_now=True,verbose_name="Fecha Devolución")
    observaciones=models.TextField(max_length=200, verbose_name="Observaciones")
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuario")
    monto=models.BigIntegerField(validators=[MinValueValidator(0)], verbose_name="Monto")
    detalleCompra=models.ForeignKey(FacturaDetalleVenta, on_delete=models.CASCADE, verbose_name="Detalle Compra")