from django.shortcuts import render

# Create your views here.
#request -> response
def login (request):
    ctx={}
    return render(request,'login.html',ctx)

def register (request):
    ctx={}
    return render(request,'register.html',ctx)