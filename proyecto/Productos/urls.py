from django.urls import path
from .views import *

urlpatterns=[
    path('productos/listar/',listar_productos, name='listar_productos'),
    path('productos/agregar/',agregar_productos, name='agregar_productos'),
    path('productos/editar/<int:idproducto>/',modificar_productos, name='modificar_productos'),
    path('productos/eliminar/<int:idproducto>/',eliminar_productos, name='eliminar_productos'),
]