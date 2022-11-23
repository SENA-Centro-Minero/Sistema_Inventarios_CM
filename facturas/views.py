from django.shortcuts import render,redirect
from facturas.models import Factura,Devolucion
from facturas.forms import FacturaForm, FacturaDetalleCompraForm,FacturaDetalleVentaForm,DevolucionForm
from usuarios.models import Usuario
from django.contrib import messages

def devolucion(request):
    devoluciones= Devolucion.objects.all()
    form= DevolucionForm()
    context={
        'form':form,
        'devoluciones':devoluciones,
    }
    return render(request,'facturas/devoluciones.html',context)
def factura(request, modal_status='hid'):
    titulo="Facturas"
    facturas= Factura.objects.filter(estado='1')

    ### cuerpo del modal ###
    modal_title= ""
    modal_txt= ""
    modal_submit= ""
    ########################

    pk_factura = ""
    tipo =None
    form_update= None
    form =FacturaForm()


    if request.method == "POST" and 'form-crear' in request.POST:
        form= FacturaForm(request.POST)
        if form.is_valid():
            aux = form.save(commit=False)
            aux.empleado=Usuario.objects.get(user_id=request.user.id)
            aux.save()
            messages.success(
                request,f"La Factura {aux.numeroSerie} ha sido abierta!"
            )
            if aux.tipoFactura == 'Venta':
                return redirect('f-d-venta', aux.numeroSerie)
            else:
                return redirect('f-d-compra', aux.numeroSerie)

            return redirect('facturas')
        else:
            form= FacturaForm(request.POST)
            messages.error(
                request,"Error al abrir la factura"
            )
########################################## Configuracion Modal de eliminacion ###############################
    if request.method == "POST" and 'form-eliminar' in request.POST:
        modal_status= 'show'
        pk_factura = request.POST['pk']
        factura= Factura.objects.get(id=pk_factura)

        ## cuerpo del modal ##
        modal_title = f"Eliminar {factura}"
        modal_txt= f"eliminar la factura {factura}"
        modal_submit="Eliminar"
        #######################

        tipo="eliminar"
########################################## Configuracion Modal de edición ###############################
    if request.method == "POST" and 'form-editar' in request.POST:
        modal_status= 'show'
        pk_factura = request.POST['pk']
        factura= Factura.objects.get(id=pk_factura)

        ## cuerpo del modal ##
        modal_title = f"Editar {factura}"
        modal_submit="Editar"
        #######################

        tipo="editar"
        form_update= FacturaUpdateForm(instance=factura)

########################################## Configuracion de eliminación ###############################
    if request.method == 'POST' and 'modal-confirmar' in request.POST:
        if request.POST['tipo'] == 'eliminar':
            factura = Factura.objects.filter(id = int(request.POST['modal-pk'])).update(
                estado='0'
            )
            messages.success(
                request,f"Se eliminó la factura {factura.nombre} exitosamente!"
            )
            return redirect('facturas')

        if request.POST['tipo'] == 'editar':
            pk_factura = request.POST['modal-pk']
            factura = Factura.objects.get(id=pk_factura)
            form_update=FacturaUpdateForm(request.POST, instance=factura)

            if form_update.is_valid():
                form_update.save()
                messages.success(
                    request,f"Se editó la factura {factura.nombre} exitosamente!"
                )
                return redirect('facturas')
        
    context={
        'titulo':titulo,
        'facturas':facturas,
        'form':form,
        'modal_status':modal_status,
        'modal_submit': modal_submit,
        'modal_title': modal_submit,
        'modal_txt': modal_txt,
        'pk': pk_factura,
        'tipo': tipo,
        'form_update':form_update

    }
    return render(request,'facturas/facturas.html',context)


def factura_detalle_compra(request,pk):
    titulo = f"Detalle de Factura de Venta {pk}"
    form= FacturaDetalleCompraForm()
    context={
        'titulo':titulo,
        'form':form,
    }
    return render(request,'facturas/factura-detalle-compra.html',context)
def factura_detalle_venta(request,pk):
    titulo = f"Detalle de Factura de Venta {pk}"
    form= FacturaDetalleVentaForm()
    context={
        'titulo':titulo,
        'form':form,
    }
    return render(request,'facturas/factura-detalle-venta.html',context)

