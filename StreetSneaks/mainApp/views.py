from django.shortcuts import render
from sneakerApp.models import Zapatilla
# Create your views here.

def index(request):
    zapatillas = Zapatilla.objects.all()
    ctx = {'items': zapatillas}
    return render(request, 'index.html', ctx)



def custom_404(request, exception):
    ctx  = {'title':'Error 404'}
    return render(request, '404.html', context=ctx)