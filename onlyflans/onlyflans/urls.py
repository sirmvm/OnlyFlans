"""onlyflans URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from web.views import agregar_producto, eliminar_producto, limpiar_producto, restar_producto
from web.views import indice,acerca,bienvenido,contacto,exito,registro,carro_compras

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',indice,name="indice"),
    path('acerca',acerca,name="acerca"),
    path('bienvenido',bienvenido,name="bienvenido"),
    path('contacto',contacto,name="contacto"),
    path('exito',exito,name="exito"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registrarse',registro,name="registro"),
    path('carrito',carro_compras,name="carrito"),
    path('agregar/<int:producto_id>',agregar_producto,name="agregar"),
    path('eliminar/<int:producto_id>',eliminar_producto,name="eliminar"),
    path('restar/<int:producto_id>',restar_producto,name="restar"),
    path('limpiar/',limpiar_producto,name="limpiar"),
    
]
