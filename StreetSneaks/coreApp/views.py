from django.shortcuts import render
from sneakerApp.models import Zapatilla
# Create your views here.
def work(request):
    zapatillas = Zapatilla.objects.all()
    ctx = {'items': zapatillas}
    return render(request, 'trabaja.html', ctx)
def tos(request):
    zapatillas = Zapatilla.objects.all()
    ctx = {'items': zapatillas}
    return render(request, 'tos.html', ctx)
def faq(request):
    zapatillas = Zapatilla.objects.all()
    ctx = {'items': zapatillas}
    return render(request, 'question.html', ctx)
def priv(request):
    zapatillas = Zapatilla.objects.all()
    ctx = {'items': zapatillas}
    return render(request, 'privacidad.html', ctx)