from django.db import models

# Create your models here.

class MensajeContacto(models.Model):
    rut = models.IntegerField(primary_key=True, verbose_name="Rut")
    asuntoMensaje = models.CharField(max_length=100, verbose_name='Asunto Mensaje')
    nombreContacto = models.CharField(max_length=40, verbose_name='Nombre de Contacto')
    correoContacto = models.EmailField(max_length=100, verbose_name='Correo de Contacto')
    fonoContacto = models.IntegerField(verbose_name='Telefono de Contacto')
    mensaje = models.CharField(max_length=500, verbose_name='Mensaje')

    def __str__(self):
        return self.asuntoMensaje


