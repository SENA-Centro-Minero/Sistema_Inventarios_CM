from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator


# Create your models here.
class Factura(models.Model):
    fecha=models.DateField(verbose_name="Fecha Factura", help_text=u"MM/DD/AAAA")
