from django.shortcuts import redirect, render
from .models import Categoria, TallaEUR
from django.contrib.auth.decorators import login_required, user_passes_test
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
def sneakUp(request):
    categoria = Categoria.objects.all()
    talla = TallaEUR.objects.all()
    ctx = {'categorias' : categoria, 'tallas': talla}
    return render(request, 'upcontent.html',ctx)


def createSneak(request):
    if request.method == 'GET':
        return redirect('crear-zapatilla') 
    else:
        name = request.POST['prod-name']
        categoria = request.POST['categoria']
        talla = request.POST['talla']
        precio = request.POST['precio']
        img = request.FILES['formFile']
        print(name, categoria, talla, precio, img)
        return redirect('crear-zapatilla')  