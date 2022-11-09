from django.urls import path

from facturas.views import factura, factura_detalle_compra,factura_detalle_venta

urlpatterns = [
    path('', factura, name="facturas"),
    path('compra/<int:pk>/',factura_detalle_compra,name="f-d-compra"),
    path('venta/<int:pk>/',factura_detalle_venta,name="f-d-venta"),

]