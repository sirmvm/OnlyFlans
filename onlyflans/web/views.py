from http.client import HTTPResponse
from django.shortcuts import render

from web.carrito import Carrito
from .models import Flan
from .models import ContactForm
from .forms import ContactFormForm, ContactFormModelForm, UserRegisterForm,forms
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib import messages



def indice(request):
    flans= Flan.objects.filter(is_private=False)
    return render(request,'index.html',{'flans':flans})

def acerca(request):
    
    return render(request,'about.html',{})

@login_required   
def bienvenido(request):
    flans= Flan.objects.filter(is_private=True)
    return render(request,'welcome.html',{'flans':flans})

def contacto(request):
    if request.method=='POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/exito')
    else:
        form=ContactFormModelForm()

    
    return render(request,'contacto.html',{'form':form})


def exito(request):
    return render(request,'success.html',{})



def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            usuario = form.cleaned_data['username']
            passw = form.cleaned_data['password1']
            new_user = authenticate(username = usuario, password = passw)
            login(request, user = new_user)
            

            messages.success(request, f'Usuario {usuario} registrado exitosamente.')
            

            return HttpResponseRedirect('/')
    else:
        form = UserRegisterForm()
    return render(request,'register.html',{'form':form})

def agregar_producto(request,producto_id):
    carrito=Carrito(request)
    producto= Flan.objects.get(id=producto_id)
    carrito.agregar(producto)
    return HttpResponseRedirect('/carrito')

def eliminar_producto(request,producto_id):
    carrito = Carrito(request)
    producto= Flan.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return HttpResponseRedirect('/carrito')

def restar_producto(request,producto_id):
    carrito = Carrito(request)
    producto= Flan.objects.get(id=producto_id)
    carrito.restar(producto)
    return HttpResponseRedirect('/carrito')

def limpiar_producto(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return HttpResponseRedirect('/carrito')

def carro_compras(request):
    
    return render(request,'carrito.html',{})