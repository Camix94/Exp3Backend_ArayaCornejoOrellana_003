from django.shortcuts import render, redirect
from .models import MensajeContacto
from .forms import MensajeForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def galeria(request):
    return render(request, 'galeria.html')


def crearMensajeNuevo(request):
    if request.method=='POST': 
        form_1 = MensajeForm(request.POST)
        if form_1.is_valid():
            form_1.save()    
            return redirect('index')
    else:
        form_1= MensajeForm()
    return render(request, 'core/form.html', {'form_1': form_1})

def Ver(request):
    mensajes = MensajeContacto.objects.all()

    return render(request, 'core/mostrar-datos-form.html', context={'mensajes':mensajes})