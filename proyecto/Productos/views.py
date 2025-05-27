from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from .forms import ProductoForm
from .models import *

# Create your views here.

def listar_productos(request):
    productos=Producto.objects.all()
    return render(request,'productos/listar.html', {'producto': productos})


def agregar_productos(request):
    form=ProductoForm()
    if request.method=='POST':
        form=ProductoForm(request.POST)
        if form.is_valid():
            Producto.objects.create(
                nombre=form.cleaned_data['nombre'],
                precio=form.cleaned_data['precio'],
                descripcion=form.cleaned_data['descripcion']
            )
            return redirect('listar_productos')
    return render(request,'productos/agregar.html',{'form':form})

def modificar_productos(request,idproducto):
    producto=get_object_or_404(Producto, idproducto=idproducto)
    form=ProductoForm(initial={
        'nombre':producto.nombre,
        'precio':producto.precio,
        'descripcion':producto.descripcion,
    })
    if request.method=='POST':
        form=ProductoForm(request.POST)
        if form.is_valid():
            producto.nombre=form.cleaned_data['nombre']
            producto.precio=form.cleaned_data['precio']
            producto.descripcion=form.cleaned_data['descripcion']
            producto.save()
            return redirect('listar_productos')
    return render(request,'productos/editar.html',{'form':form})

def eliminar_productos(request,idproducto):
    producto=get_object_or_404(Producto,idproducto=idproducto)
    if request.method=='POST':
        producto.delete()
        return redirect('listar_productos')
    return render(request,'productos/eliminar.html',{'producto':producto})