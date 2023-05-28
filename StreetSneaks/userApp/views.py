from django.shortcuts import redirect, render, get_object_or_404
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from userApp.models import Usuario
from django.contrib import messages
from django.contrib.auth.decorators import login_required




# Create your views here.
#request -> response
def errors(request):
    return render(request, 'not_found.html')


@login_required
def profile(request):
    ctx = {}
    return render(request, 'profile.html', ctx)


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