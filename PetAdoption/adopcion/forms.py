from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import MensajeContacto

class MensajeForm(forms.ModelForm):

    class Meta: 
        model= MensajeContacto
        fields = ['rut','asuntoMensaje', 'nombreContacto', 'correoContacto', 'fonoContacto', 'mensaje']
        labels ={
            'rut' : 'Rut',
            'asuntoMensaje' : 'Asunto' ,
            'nombreContacto' : 'Nombre', 
            'correoContacto' : 'Correo', 
            'fonoContacto' : 'Teléfono', 
            'mensaje' : 'Mensaje',
        }
        widgets={
            'rut': forms.NumberInput(
                attrs={
                    'class': 'details',
                    'placeholder': 'Ingrese su rut', 
                    'name': 'rut',
                    'id' : 'rut'
                }
            ),
            'asuntoMensaje': forms.TextInput(
                attrs={
                    'class': 'details', 
                    'placeholder': 'Ingrese asunto del mensaje', 
                    'name': 'asuntoMensaje',
                    'id' : 'asuntoMensaje'
                }
            ), 
            'nombreContacto': forms.TextInput(
                attrs={
                    'class': 'details', 
                    'placeholder': 'Ingrese su nombre', 
                    'name': 'nombreContacto',
                    'id' : 'nombreContacto'
                }
            ), 
            'correoContacto': forms.EmailInput(
                attrs={
                    'class' : 'details', 
                    'placeholder': 'Ingrese correo', 
                    'name': 'correoContacto',
                    'id' : 'correoContacto'
                }
            ), 
            'fonoContacto': forms.NumberInput(
                attrs={
                    'class': 'details',
                    'placeholder': 'Ingrese teléfono', 
                    'name': 'fonoContacto',
                    'id' : 'fonoContacto'
                }
            ),
            'mensaje': forms.Textarea(
                attrs={
                    'class': 'details',
                    'placeholder': 'Ingrese mensaje', 
                    'name': 'mensaje',
                    'id' : 'mensaje'
                }
            )

        }