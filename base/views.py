from django.shortcuts import render, redirect

def inicioAdmin(request):
    titulo="Tablero Principal"
    context={
        'titulo':titulo
    }
    return render(request,'index-admin.html', context)