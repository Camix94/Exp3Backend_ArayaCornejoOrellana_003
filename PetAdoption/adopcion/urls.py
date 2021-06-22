from django.urls import path
from .views import index,galeria,crearMensajeNuevo, Ver

urlpatterns=[
    path('',index, name='index'),
    path('galeria', galeria, name='galeria'),
    path('crear_mensaje_nuevo', crearMensajeNuevo, name="crearMensajeNuevo"),
    path('ver', Ver, name="ver")
]