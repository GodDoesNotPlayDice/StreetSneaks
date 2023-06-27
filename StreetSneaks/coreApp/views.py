import time
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from ventaApp.models import Boleta
from userApp.models import Usuario
from .models import Contactanos
from sneakerApp.models import Zapatilla
# Create your views here.
@login_required
def work(request):
    zapatillas = Zapatilla.objects.all()
    ctx = {'items': zapatillas}
    return render(request, 'trabaja.html', ctx)

def tos(request):
    zapatillas = Zapatilla.objects.all()
    ctx = {'items': zapatillas}
    return render(request, 'tos.html', ctx)

@login_required
def faq(request):
    orders = Boleta.objects.filter(user=request.user)
    ctx = {'orders': orders}
    return render(request, 'question.html', ctx)

@login_required
def enviarForm(request):
    if request.method == 'POST':
        nombre = request.POST.get('name')
        try:
            surname = request.POST.get('surname')
        except:
            surname = None
        
        try:
            celular = request.POST.get('numero')
        except:
            celular = None
        
        email = request.POST.get('email')

        try:
            nro_pedido = request.POST.get('order')
        except:
            nro_pedido = None
        
        try:
            asunto = request.POST.get('subject')
        except:
            asunto = None
        
        try:
            mensaje = request.POST.get('message')
        except:
            mensaje = None
        
        try:
            propuesta = request.POST.get('propuesta')
        except:
            propuesta = None

        contacto = Contactanos(nombre=nombre, surname=surname, celular=celular , email=email, nro_pedido=nro_pedido, asunto=asunto, mensaje=mensaje, propuesta=propuesta)
        contacto.save()
        time.sleep(2)
        if not request.user.is_superuser:
            return redirect('index')
        else:
            return redirect('respuestas')
    else:
        return render(request, 'contactanos.html')


@login_required
@user_passes_test(lambda user: user.is_superuser)
def respuestas(request):
    preguntas = Contactanos.objects.all()
    ctx = {'preguntas': preguntas, 'title': 'Preguntas y Trabajo'}
    return render(request, 'respuestas.html', ctx)


def priv(request):
    zapatillas = Zapatilla.objects.all()
    ctx = {'items': zapatillas}
    return render(request, 'privacidad.html', ctx)

