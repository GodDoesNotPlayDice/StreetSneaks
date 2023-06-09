import time
from django.shortcuts import redirect, render, get_object_or_404
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from ventaApp.models import Venta, Boleta
from userApp.models import Carro
from userApp.models import Usuario, Direccion, Region
from django.contrib import messages
from django.contrib.auth.decorators import login_required



@login_required
def save_direccion(request):
    if request.method == 'POST':
        region = request.POST['region']
        region = Region.objects.get(id=region)
        Direccion(region=region, user=request.user, direccion=request.POST['direccion']).save()
        return redirect('profile')
    
    
@login_required
def del_direccion(request, id_direccion):
    direc = Direccion.objects.get(pk=id_direccion)
    Carro.objects.filter(direccion=direc).update(direccion=None)
    direc.delete()
    return redirect('profile')



@login_required
def edit_direccion(request, id_direccion):
    direc = Direccion.objects.get(pk=id_direccion)
    regiones = Region.objects.all()
    ctx = {'direccion': direc,'regiones': regiones, 'title': 'Editar direccion'}
    return render(request, 'direccion_editar.html', ctx)


@login_required
def edi_direct(request, id_direccion):
    direc = Direccion.objects.get(pk=id_direccion)
    if request.method == 'POST':
        if request.POST['nueva_direccion'] != '':
            direc.direccion = request.POST['nueva_direccion']
        direc.region = Region.objects.get(pk=request.POST['region'])
        direc.save()
        return redirect('profile')

@login_required
def profile(request):
    ventas = Venta.objects.all()
    boleta = Boleta.objects.filter(user=request.user)
    regiones = Region.objects.all()
    direcciones = Direccion.objects.filter(user=request.user)
    ctx = {'regiones': regiones, 'title': request.user.username, 'direcciones': direcciones, 'ventas' : ventas, 'boleta': boleta}
    return render(request, 'profile.html', ctx)

@login_required
def carro(request, username):
    prods = 0
    total_precio = 0
    carro = Carro.objects.filter(user=request.user)
    direcciones =  Direccion.objects.filter(user=request.user)
    for i in carro:
       total_precio += i.items.precio
       prods+=1
    ctx = {'username': username, 'carro': carro, 'total_prods':prods, 'total_precio': total_precio, 'direcciones' : direcciones, 'title': 'Carro'}
    return render(request, 'carro.html', ctx)


def signup(request):

    ctx={'title': 'Register'}
    if request.method == 'GET':
        return render(request, 'register.html', ctx)
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
                return render(request,'register.html', ctx)
        else:
            messages.warning(request, 'Password no coinciden')
            return render(request,'register.html', ctx)
        
def signin(request):
        ctx = {'title' : 'Login'}
        if request.method == 'GET':
            return render(request, 'login.html', ctx)
        else:
            user = authenticate(request, username=request.POST['usuario'], password=request.POST['password'])
            if user is None:
                return render(request, 'login.html', {'error': 'error', 'title':'Login'})
            else:
                login(request, user)
                print(request.POST)
                return redirect('profile')

def signout(request):
    logout(request)
    return redirect('index')

@login_required
def goEdit(request):
    try:
        usuario = Usuario.objects.get(user=request.user)
    except:
        usuario = None
    ctx = {'title': 'Editar perfil', 'usuario': usuario}
    return render(request, 'editar_user.html', ctx)

@login_required
def editarUsuario(request):
    if request.method == 'POST':
        user = User.objects.get(username=request.user.username)
        usuario = Usuario.objects.get(user=request.user)
        if request.POST['username'] != '':
            user.username = request.POST['username']
        if request.POST['email'] != '':
            user.email = request.POST['email']
        if request.POST['lastname'] != '':
            user.last_name = request.POST['lastname']
        if request.POST['celular'] != '':
            usuario.celular = request.POST['celular']
        usuario.save()
        user.save()
        time.sleep(2)
        return redirect('profile')