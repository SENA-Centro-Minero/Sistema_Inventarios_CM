from django.shortcuts import render, redirect
from django.views.defaults import page_not_found
from usuarios.models import Municipio
def inicio(request):
    
    context={
    }
    return render(request,'login.html', context)

def inicioAdmin(request):
    titulo="Tablero Principal"
    context={
        'titulo':titulo
    }
    return render(request,'index-admin.html', context)

def municipio(request):
    titulo="Municipios"
    municipios=Municipio.objects.all()
    context={
        'titulo':titulo,
        'municipios':municipios
    }
    return render(request,'usuarios/municipios.html',context)
def departamento(request):
    titulo="Departamentos"

    context={
        'titulo':titulo
    }
    return render(request,'usuarios/departamentos.html',context)

def error_404(request,exception):
    return page_not_found(request,'404.html')

def contacto(request):
    context={}
    return render(request,'contacto.html',context)