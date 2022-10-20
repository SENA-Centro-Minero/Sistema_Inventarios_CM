from django.shortcuts import redirect, render

from usuarios.forms import UsuarioForm, EmpresaForm, EmpresaUpdateForm
from usuarios.models import Usuario,Empresa

from django.contrib import messages

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
    return render(request,'partials/crear.html',context)
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
    return render(request,'partials/crear.html',context)
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

def empresas(request, modal_status='hid'):
    titulo="Empresas"
    empresas= Empresa.objects.filter(estado='1')

    ### cuerpo del modal ###
    modal_title= ""
    modal_txt= ""
    modal_submit= ""
    ########################

    pk_empresa = ""
    tipo =None
    form_update= None
    form =EmpresaForm()


    if request.method == "POST" and 'form-crear' in request.POST:
        form= EmpresaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('empresas')
        else:
            form= EmpresaForm(request.POST)
            messages.error(
                request,"Error al agregar la empresa"
            )
########################################## Configuracion Modal de eliminacion ###############################
    if request.method == "POST" and 'form-eliminar' in request.POST:
        modal_status= 'show'
        pk_empresa = request.POST['pk']
        empresa= Empresa.objects.get(id=pk_empresa)

        ## cuerpo del modal ##
        modal_title = f"Eliminar {empresa}"
        modal_txt= f"eliminar la empresa {empresa}"
        modal_submit="Eliminar"
        #######################

        tipo="eliminar"
########################################## Configuracion Modal de edición ###############################
    if request.method == "POST" and 'form-editar' in request.POST:
        modal_status= 'show'
        pk_empresa = request.POST['pk']
        empresa= Empresa.objects.get(id=pk_empresa)

        ## cuerpo del modal ##
        modal_title = f"Editar {empresa}"
        modal_submit="Editar"
        #######################

        tipo="editar"
        form_update= EmpresaUpdateForm(instance=empresa)

########################################## Configuracion de eliminación ###############################
    if request.method == 'POST' and 'modal-confirmar' in request.POST:
        if request.POST['tipo'] == 'eliminar':
            empresa = Empresa.objects.filter(id = int(request.POST['modal-pk'])).update(
                estado='0'
            )
            messages.success(
                request,f"Se eliminó la empresa {empresa.nombre} exitosamente!"
            )
            return redirect('empresas')

        if request.POST['tipo'] == 'editar':
            pk_empresa = request.POST['modal-pk']
            empresa = Empresa.objects.get(id=pk_empresa)
            form_update=EmpresaUpdateForm(request.POST, instance=empresa)

            if form_update.is_valid():
                form_update.save()
                messages.success(
                    request,f"Se editó la empresa {empresa.nombre} exitosamente!"
                )
                return redirect('empresas')
        
    context={
        'titulo':titulo,
        'empresas':empresas,
        'form':form,
        'modal_status':modal_status,
        'modal_submit': modal_submit,
        'modal_title': modal_submit,
        'modal_txt': modal_txt,
        'pk': pk_empresa,
        'tipo': tipo,
        'form_update':form_update

    }
    return render(request,'usuarios/empresas.html',context)

