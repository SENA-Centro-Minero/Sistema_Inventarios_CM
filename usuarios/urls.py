from django.urls import path

from usuarios.views import empresas,empresas_editar,empresas_eliminar

from usuarios.views import usuarios, usuarios_crear,usuarios_editar,usuarios_eliminar
urlpatterns = [
    path('usuario/',usuarios,name="usuarios"),
    path('usuario-crear/',usuarios_crear,name="usuarios-crear"),
    path('usuario-editar/<int:pk>/',usuarios_editar,name="usuarios-editar"),
    path('usuario-eliminar/<int:pk>/',usuarios_eliminar,name="usuarios-eliminar"),

    path('empresa/',empresas,name="empresas"),
    path('empresa-editar/<int:pk>/',empresas_editar,name="empresas-editar"),
    path('empresa-eliminar/<int:pk>/',empresas_eliminar,name="empresas-eliminar"),


    path('empresa/',empresas,name="empresas"),


]
