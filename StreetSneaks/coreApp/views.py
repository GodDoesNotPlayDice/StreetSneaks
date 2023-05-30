from django.shortcuts import render
from mainApp.views import ZAPATILLA
# Create your views here.
def work(request):
    ctx = {'items': ZAPATILLA}
    return render(request, 'trabaja.html', ctx)
def tos(request):
    ctx = {'items': ZAPATILLA}
    return render(request, 'tos.html', ctx)
def faq(request):
    ctx = {'items': ZAPATILLA}
    return render(request, 'question.html', ctx)
def priv(request):
    ctx = {'items': ZAPATILLA}
    return render(request, 'privacidad.html', ctx)