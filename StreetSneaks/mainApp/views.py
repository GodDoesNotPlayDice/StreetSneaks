from django.shortcuts import render
from sneakerApp.models import Zapatilla
# Create your views here.

def index(request):
    zapatillas = Zapatilla.objects.all()
    ctx = {'items': zapatillas}
    return render(request, 'index.html', ctx)