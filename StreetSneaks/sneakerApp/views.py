import os
from django.conf import settings
from django.shortcuts import redirect, render
from .models import Categoria, TallaEUR
from django.contrib.auth.decorators import login_required, user_passes_test
# from django.core.files.storage import default_storage
from .models import Zapatilla, TallaEUR, Categoria

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



@login_required
@user_passes_test(lambda user: user.is_superuser)
def sneaks(request):
    categoria = Categoria.objects.all()
    talla = TallaEUR.objects.all()
    items = Zapatilla.objects.all()
    ctx = {'categorias' : categoria, 'tallas': talla, 'zapatillas': items}
    return render(request, 'crud.html',ctx)

@login_required
@user_passes_test(lambda user: user.is_superuser)
def createSneak(request):
    if request.method == 'POST':
        name = request.POST['name']
        categoria = request.POST['categoria']
        talla = request.POST['talla']
        precio = request.POST['precio']
        img = request.FILES['file_input']
        print(name, categoria, talla, precio, img)
        categoria = Categoria.objects.get(id=categoria)
        talla = TallaEUR.objects.get(id=talla)
        nueva_zapatilla = Zapatilla(
            name=name,
            imagen=img,
            precio=precio,
            disponible=True,
            tallaEUR=talla,
            categoria=categoria
        )
        nueva_zapatilla.save()
        return redirect('gestion-zapatillas')  
    else:
        return redirect('gestion-zapatillas') 

@login_required
@user_passes_test(lambda user: user.is_superuser)
def deleteSneak(request,id):
    zapatilla = Zapatilla.objects.get(pk=id)
    zapatilla.delete()
    del zapatilla
    return redirect('gestion-zapatillas')