from django.urls import path
from .views import index,galeria,crearMensajeNuevo, Ver, form_mod_mensaje, eliminar_mensaje

urlpatterns=[
    path('',index, name='index'),
    path('galeria', galeria, name='galeria'),
    path('crear_mensaje_nuevo', crearMensajeNuevo, name="crearMensajeNuevo"),
    path('ver', Ver, name="ver"),
    path('modificar_mensaje/<id>', form_mod_mensaje, name="modificar_mensaje"),
    path('eliminar_mensaje/<id>', eliminar_mensaje, name="eliminar_mensaje") 
]