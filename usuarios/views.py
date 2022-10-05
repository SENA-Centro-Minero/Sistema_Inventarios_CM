from django.shortcuts import render

# Create your views here.
def usuarios(request):
    context={

    }
    return render(request,'usuarios/usuarios.html',context)
