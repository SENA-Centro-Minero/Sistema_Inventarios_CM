from django.shortcuts import render, redirect
from django.views.defaults import page_not_found
from usuarios.models import Municipio, Departamento
from usuarios.forms import DepartamentoForm,MunicipioForm
from django.contrib import messages
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
            messages.success(
                request,f"Se agregó el municipio de {request.POST['nombre']} exitosamente!"
            )
            return redirect('municipio')
        else:
            messages.error(
                request,f"Error al agregar {request.POST['nombre']}!"
            )
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
            messages.success(
                request,f"Se agregó el departamento de {request.POST['nombre']} exitosamente!"
            )
            return redirect('departamento')
        else:
            messages.error(
                request,f"Error al agregar {request.POST['nombre']}!"
            )
    else:
        form= DepartamentoForm()
    context={
        'titulo':titulo,
        'departamentos':departamentos,
    }
    return render(request,'usuarios/departamentos.html',context)

def departamento_eliminar(request,pk):
    titulo="Departamentos"
    
    departamento=Departamento.objects.filter(id=pk).delete()
    messages.success(
            request,f"Se eliminó el departamento exitosamente!"
        )
    return redirect('departamento')
    
    context={
        'titulo':titulo,
        
    }
    return render(request,'usuarios/departamentos.html',context)
def error_404(request,exception):
    return page_not_found(request,'404.html')

def contacto(request):
    context={}
    return render(request,'contacto.html',context)