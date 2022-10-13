from django.shortcuts import render

# Create your views here.

def producto(request):
    titulo= 'producto'

    productos= Producto.objects.all()


    context={
    'titulo':titulo,
    'productos':productos
    }
    return render(request,'productos/producto.html',context)