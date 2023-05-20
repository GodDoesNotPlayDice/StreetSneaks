from django.shortcuts import render

# Create your views here.
def work(request):
    ctx = {}
    return render(request, 'trabaja.html', ctx)
def tos(request):
    ctx = {}
    return render(request, 'tos.html', ctx)
def faq(request):
    ctx = {}
    return render(request, 'question.html', ctx)
def priv(request):
    ctx = {}
    return render(request, 'privacidad.html', ctx)