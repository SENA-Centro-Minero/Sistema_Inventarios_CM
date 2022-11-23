from django.shortcuts import render, redirect
from django.views.defaults import page_not_found
from usuarios.models import Municipio, Departamento
from usuarios.forms import DepartamentoForm,MunicipioForm
from django.contrib import messages
from django.contrib.auth import logout
from productos.models import Producto
from usuarios.models import Usuario
from facturas.models import Factura, Devolucion

def inicioAdmin(request):
    titulo="Tablero Principal"
    cantidad_productos= Producto.objects.all().count()
    cantidad_usuarios= Usuario.objects.all().count()
    cantidad_facturas= Factura.objects.all().count()
    cantidad_devoluciones= Devolucion.objects.all().count()

    labels_stock=[]
    data_stock=[]
    productos= Producto.objects.all().order_by('stock')
    for producto in productos:
        labels_stock.append(producto.nombre)
        data_stock.append(producto.stock)

    context={
        'titulo':titulo,
        'cantidad_usuarios':cantidad_usuarios,
        'cantidad_productos':cantidad_productos,
        'cantidad_facturas':cantidad_facturas,
        'cantidad_devoluciones':cantidad_devoluciones,
        'labels_stock': labels_stock,
        'data_stock':data_stock,
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

# def loggedIn(request):
#     if request.user.is_authenticated:
#         respuesta:"Ingresado como "+ request.user.username
#     else:
#         respuesta:"No estas autenticado."
#     return HttpResponse(respuesta)

def logout_user(request):
    logout(request)
    return redirect('inicio')