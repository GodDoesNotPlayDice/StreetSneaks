from django.shortcuts import get_object_or_404, redirect, render
from sneakerApp.models import Zapatilla
from userApp.models import Carro
# Create your views here.

def agregar_carro(request, id_prod):
    zapatilla = get_object_or_404(Zapatilla, id=id_prod)
    Carro(user=request.user, items=zapatilla).save()
    return redirect('carro', username=request.user.username)


