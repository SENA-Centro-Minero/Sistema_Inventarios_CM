from django.shortcuts import redirect, render

from usuarios.forms import UsuarioForm,EmpresaForm
from usuarios.models import Usuario,Empresa

# Create your views here.
def usuarios(request):
    titulo="Usuarios"
    usuarios= Usuario.objects.all()
    context={
        'titulo':titulo,
        'usuarios':usuarios
    }
    return render(request,'usuarios/usuarios.html',context)

def usuarios_crear(request):
    titulo="Usuarios - Crear"
    if request.method == "POST":
        form= UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
        else:
            print("Error")
    else:
        form= UsuarioForm()
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'usuarios/usuarios-crear.html',context)
def usuarios_editar(request, pk):
    titulo="Usuarios - Editar"
    usuario= Usuario.objects.get(id=pk)
    if request.method == "POST":
        form= UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
        else:
            print("Error al guardar")
    else:
        form= UsuarioForm(instance=usuario)
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'usuarios/usuarios-crear.html',context)
def usuarios_eliminar(request, pk):
    titulo="Usuarios - Eliminar"
    usuarios= Usuario.objects.all()

    Usuario.objects.filter(id=pk).update(
            estado='0'
        )
    return redirect('usuarios')
        
   
    context={
        'usuarios':usuarios,
        'titulo':titulo,
     
    }
    return render(request,'usuarios/usuarios.html',context)

def empresas(request):
    titulo="Empresas"
    empresas= Empresa.objects.all()
    if request.method == "POST":
        form= EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empresas')
        else:
            print("Error")
    else:
        form= EmpresaForm()
  
    context={
        'titulo':titulo,
        'empresas':empresas,
        'form':form

    }
    return render(request,'usuarios/empresas.html',context)



def empresas_editar(request, pk):
    titulo="Empresas - Editar"
    empresa= Empresa.objects.get(id=pk)
    if request.method == "POST":
        form= EmpresaForm(request.POST, intance=empresa)
        if form.is_valid():
            form.save()
            return redirect('empresas')
        else:
            print("Error al guardar")
    else:
        form= EmpresaForm(instance=empresa)
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'usuarios/empresas-crear.html',context)
def empresas_eliminar(request, pk):
    titulo="Empresas - Eliminar"
    empresas= Empresa.objects.all()

    Empresa.objects.filter(id=pk).update(
            estado='0'
        )
    return redirect('empresas')
        
   
    context={
        'empresas':empresas,
        'titulo':titulo,
     
    }
    return render(request,'empresas/empresas.html',context)