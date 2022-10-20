from django.urls import path



from productos.views import productos, productos_crear,productos_editar,productos_eliminar
urlpatterns = [
    path('producto/',productos,name="productos"),
    path('producto-crear/',productos_crear,name="productos-crear"),
    path('producto-editar/<int:pk>/',productos_editar,name="productos-editar"),
    path('producto-eliminar/<int:pk>/',productos_eliminar,name="productos-eliminar"),
]