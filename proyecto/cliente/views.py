from django.shortcuts import render,redirect,get_object_or_404
from cliente.forms import ClienteForm
from cliente.models import Cliente
# Create your views here.
def inicio(request):
    return render (request,('inicio.html'))
def agregar_cliente(request):
    form=ClienteForm()
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('Lista')
    return render(request,('Agregar.html'),{'form' : form})

def eliminar_cliente(request,pk):
    clientes = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        clientes.delete()
        return redirect('Lista')
    
    return render(request,('Eliminar.html'),{'Cliente': clientes})

def modificar_cliente(request, pk):
    clientes = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=clientes)
        if form.is_valid():
            form.save()
            return redirect('Lista')
    else:
        form = ClienteForm(instance=clientes)
    return render(request,('Modificar.html'),{'form':form , 'Cliente':clientes})

def lista_cliente(request):
    clientes = Cliente.objects.all()
    return render(request,('Lista.html'),{'Cliente':clientes})
