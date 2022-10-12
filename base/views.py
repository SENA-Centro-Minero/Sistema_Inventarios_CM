from django.shortcuts import render, redirect
from django.views.defaults import page_not_found
from usuarios.models import Municipio, Departamento
from usuarios.forms import DepartamentoForm,MunicipioForm

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
    departamentos=Departamento.objects.all()

    if request.method == "POST":
        form= MunicipioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('municipio')
        else:
            print("No se pudo agregar el departamento")
    else:
        form= MunicipioForm()
    context={
        'titulo':titulo,
        'municipios':municipios,
        'departamentos':departamentos,

    }
    return render(request,'usuarios/municipios.html',context)
def departamento(request):
    titulo="Departamentos"
    departamentos=Departamento.objects.all()
    if request.method == "POST":
        form= DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('departamento')
        else:
            print("No se pudo agregar el departamento")
    else:
        form= DepartamentoForm()
    context={
        'titulo':titulo,
        'departamentos':departamentos,
    }
    return render(request,'usuarios/departamentos.html',context)

def error_404(request,exception):
    return page_not_found(request,'404.html')

def contacto(request):
    context={}
    return render(request,'contacto.html',context)