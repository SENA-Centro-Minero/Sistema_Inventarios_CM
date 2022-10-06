from django.shortcuts import render

# Create your views here.
def usuarios(request):
    titulo="Usuarios"
    context={
        'titulo':titulo
    }
    return render(request,'usuarios/usuarios.html',context)
