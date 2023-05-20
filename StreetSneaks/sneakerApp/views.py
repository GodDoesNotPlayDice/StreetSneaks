from django.shortcuts import render

# Create your views here.
def novedades(request):
    ctx = {'title': 'Novedades' }
    return render(request, 'sneaks.html', ctx)
def hombre(request):
    ctx = {'title': 'Hombre'}
    return render(request, 'sneaks.html', ctx)
def nino(request):
    ctx = {'title': 'Niño'}
    return render(request, 'sneaks.html', ctx)
def mujer(request):
    ctx = {'title': 'Mujer'}
    return render(request, 'sneaks.html', ctx)
def deportivo(request):
    ctx = {'title': 'Deportivo'}
    return render(request, 'sneaks.html', ctx)