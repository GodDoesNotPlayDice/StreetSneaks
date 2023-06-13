import os
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
# from django.core.files.storage import default_storage
from .models import Zapatilla, TallaEUR, Categoria
from ventaApp.models import Cupon
from .functions import id_prod

# Create your views here.
def items():
    
    return Zapatilla.objects.all()    
def novedades(request):
    ctx = {'title': 'Novedades','zapatillas': items()} 
    return render(request, 'sneaks.html', ctx)
def hombre(request):
    ctx = {'title': 'Hombre','zapatillas': items()}
    return render(request, 'sneaks.html', ctx)
def nino(request):
    ctx = {'title': 'Niño','zapatillas': items()}
    return render(request, 'sneaks.html', ctx)
def mujer(request):
    ctx = {'title': 'Mujer','zapatillas': items()}
    return render(request, 'sneaks.html', ctx)

@login_required
@user_passes_test(lambda user: user.is_superuser)
def sneaks(request):
    categoria = Categoria.objects.all()
    talla = TallaEUR.objects.all()
    items = Zapatilla.objects.all()
    cupones = Cupon.objects.all()
    ctx = {'categorias' : categoria, 'tallas': talla, 'zapatillas': items, 'cupones': cupones, 'title': 'ADMIN'}
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
        img1 = request.FILES['file_input1']
        img2 = request.FILES['file_input2']
        categoria = Categoria.objects.get(id=categoria)
        talla = TallaEUR.objects.get(id=talla)
        nueva_zapatilla = Zapatilla(
            id_prod=id_prod(),
            name=name,
            imagen=img,
            imagen_muestra = img1,
            imagen_muestra_2 = img2,
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
    return redirect('gestion-zapatillas')

def editar_zapatilla(request, id):
    try:
        categoria = Categoria.objects.all()
        talla = TallaEUR.objects.all()
        zapatilla = Zapatilla.objects.get(pk=id)
        return render(request, 'modify.html', {'zapatilla': zapatilla, 'talla': talla, 'categoria': categoria})
    except Exception as e:
        print(e)       

def editSneak(request, id):
    if request.method == 'POST':
        zapatilla = Zapatilla.objects.get(pk=id)
        if request.POST['name_editar'] != '':
            zapatilla.name = request.POST['name_editar']
        if request.POST['precio_editar'] != '':
            zapatilla.precio = request.POST['precio_editar']
        if request.POST['categoria_editar'] != zapatilla.tallaEUR.pk:
            zapatilla.categoria = Categoria.objects.get(id=request.POST['categoria_editar'])
        zapatilla.tallaEUR = TallaEUR.objects.get(id=request.POST['talla_editar'])
        zapatilla.save()
        return redirect('gestion-zapatillas')


def sneak_details(request, nombre, sneak_id):
    sneak = get_object_or_404(Zapatilla, id_prod=sneak_id)
    ctx = {'sneak' : sneak, 'title': sneak.name}
    return render(request, 'details.html', ctx) 