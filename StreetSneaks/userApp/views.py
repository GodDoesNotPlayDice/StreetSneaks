from django.shortcuts import redirect, render
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


# Create your views here.
#request -> response

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
                user = User.objects.create_user (username=username, password=password, email=email)
                #messages.success(request, 'Te has registrado con exito ', user.id)
                user.save()
                login(request=request, user=user)
                return redirect('profile')
            except IntegrityError:
                return render(request,'register.html')
        else:
            return render(request,'register.html')
        
def signin(request):
    ctx = {}
    return render(request, 'login.html', ctx)