from django.urls import path
from cliente import views

urlpatterns = [
    path('',views.inicio, name ='inicio'),
    path('clientes/',views.lista_cliente, name ='Lista'),
    path('registrar/',views.agregar_cliente, name ='Agregar'),
    path('modificar/<int:pk>',views.modificar_cliente, name ='Modificar'),
    path('eliminar/<int:pk>',views.eliminar_cliente, name ='Eliminar'),
]