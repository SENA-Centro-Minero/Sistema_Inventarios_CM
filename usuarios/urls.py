from django.urls import path

from usuarios.views import empresas

from usuarios.views import usuarios, usuarios_crear,usuarios_editar,usuarios_eliminar
urlpatterns = [
    path('usuario/',usuarios,name="usuarios"),
    path('usuario-crear/',usuarios_crear,name="usuarios-crear"),
    path('usuario-editar/<int:pk>/',usuarios_editar,name="usuarios-editar"),
    path('usuario-eliminar/<int:pk>/',usuarios_eliminar,name="usuarios-eliminar"),

    path('empresa/',empresas,name="empresas"),
    path('empresa/<str:modal_status>',empresas,name="empresas"),
   


    path('empresa/',empresas,name="empresas"),


]
