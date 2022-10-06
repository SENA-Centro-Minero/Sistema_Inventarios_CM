from django.shortcuts import redirect, render

from usuarios.forms import UsuarioForm
from usuarios.models import Usuario

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