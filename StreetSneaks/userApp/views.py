from django.shortcuts import redirect, render, get_object_or_404
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from userApp.models import Carro
from userApp.models import Usuario, Direccion, Region
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from .models import Carro
from sneakerApp.models import Zapatilla




# Create your views here.
#request -> response


# @login_required
# def agregar_al_carrito(request, producto_id):
#     carro = get_object_or_404(Carro, user=request.user)
#     producto = get_object_or_404(Zapatilla, id=producto_id)
    
#     carro.items.append(producto_id)
#     carro.save()
    
#     return redirect('carro')

# @login_required
# def eliminar_del_carrito(request, producto_id):
#     carro = get_object_or_404(Carro, user=request.user)
    
#     carro.items.remove(producto_id)
#     carro.save()
    
#     return redirect('carro')



@login_required
def save_direccion(request):
    if request.method == 'POST':
        region = request.POST['region']
        region = Region.objects.get(id=region)
        Direccion(region=region, user=request.user, direccion=request.POST['direccion']).save()
        return redirect('profile')

@login_required
def profile(request):
    regiones = Region.objects.all()
    direcciones = Direccion.objects.filter(user=request.user)  # Filtrar por el usuario actual
    ctx = {'regiones': regiones, 'title': request.user.username, 'direcciones': direcciones}
    return render(request, 'profile.html', ctx)

@login_required
def carro(request, username):
    prods = 0
    total_precio = 0
    carro = Carro.objects.filter(user=request.user)
    for i in carro:
       total_precio += i.items.precio
       prods+=1
    ctx = {'username': username, 'carro': carro, 'total_prods':prods, 'total_precio': total_precio}
    return render(request, 'carro.html', ctx)


def signup(request):
    ctx={}
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                username = request.POST['name']
                password = request.POST['password1']
                email = request.POST['email']
                last_name = request.POST['apellido']
                user = User.objects.create_user (username=username.capitalize(), password=password, email=email, last_name=last_name.capitalize())
                user.save()
                user_ext = Usuario(celular=request.POST['celular'], user=user)
                user_ext.save()
                login(request=request, user=user)
                messages.success(request, 'Te has registrado con exito')
                return redirect('profile')
            except IntegrityError:
                messages.error(request, 'Ocurrio un error en el servidor')
                return render(request,'register.html')
        else:
            messages.warning(request, 'Password no coinciden')
            return render(request,'register.html')
        
def signin(request):
        ctx = {}
        if request.method == 'GET':
            return render(request, 'login.html', ctx)
        else:
            user = authenticate(request, username=request.POST['usuario'], password=request.POST['password'])
            if user is None:
                return render(request, 'login.html', {'error': 'error'})
            else:
                login(request, user)
                print(request.POST)
                return redirect('profile')

def signout(request):
    logout(request)
    return redirect('index')