from django.urls import path
from usuario import views

urlpatterns = [
    path('crerusuario/',views.crearUsuario, name ='inscribirse'),
    path('sesion/', views.inicioSesion, name='iniciosesion'),
    path('cerrar/', views.cerrarSesion, name='cerrarsesion'),
    ]