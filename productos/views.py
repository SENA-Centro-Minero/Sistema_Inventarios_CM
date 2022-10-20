from django.shortcuts import render, redirect
from productos.models import Producto
from productos.forms import ProductoForm
# Create your views here.

def productos(request):
    titulo= 'Producto'

    productos= Producto.objects.all()


    context={
    'titulo':titulo,
    'productos':productos
    }
    return render(request,'productos/productos.html',context)
def productos_crear(request):
    titulo="Productos - Crear"
    if request.method == "POST":
        form= ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('productos')
        else:
            print("Error")
    else:
        form= ProductoForm()
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'partials/crear.html',context)
def productos_editar(request, pk):
    titulo="Productos - Editar"
    producto= Producto.objects.get(id=pk)
    if request.method == "POST":
        form= ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('productos')
        else:
            print("Error al guardar")
    else:
        form= ProductoForm(instance=producto)
    context={
        'titulo':titulo,
        'form':form
    }
    return render(request,'partials/crear.html',context)
def productos_eliminar(request, pk):
    titulo="Productos - Eliminar"
    productos= Producto.objects.all()

    Producto.objects.filter(id=pk).update(
            estado='0'
        )
    return redirect('productos')
        
   
    context={
        'productos':productos,
        'titulo':titulo,
     
    }
    return render(request,'productos/productos.html',context)