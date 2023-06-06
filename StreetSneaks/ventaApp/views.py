from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.http import JsonResponse
from sneakerApp.models import Zapatilla
from userApp.models import Carro
from .models import Cupon
from mainApp.templatetags.filters import precio

# Create your views here.

@login_required
def agregar_carro(request, id_prod):
    zapatilla = get_object_or_404(Zapatilla, id=id_prod)
    Carro(user=request.user, items=zapatilla).save()
    return redirect('carro', username=request.user.username)

@login_required
def eliminar_carro(request, carro_id):
    carro = Carro.objects.get(id=carro_id, user=request.user)
    carro.delete()
    return redirect('carro', username=request.user.username)

@login_required
@user_passes_test(lambda user: user.is_superuser)
def agregar_cupon(request):
    if request.method == 'POST':
        Cupon(
            name=request.POST['nombre'],
            valor=request.POST['valor']
        ).save()
    return redirect('gestion-zapatillas')

@login_required
@user_passes_test(lambda user: user.is_superuser)
def eliminar_cupon(request, id_cupon):
    cupon = Cupon.objects.get(pk=id_cupon)
    cupon.delete()
    del cupon
    return redirect('gestion-zapatillas')

@login_required
def validar_cupon(request):
    if request.method == 'POST':
        context = {}
        cuponText = request.POST['name']
        try:
            # user = User.objects.get(username=request.user.username)
            carro = Carro.objects.filter(user=request.user)
            monto = 0
            cupon = Cupon.objects.get(name=cuponText)
            for c in carro:
                monto += c.items.precio
                c.cupon = cupon
                c.save()
            total = monto - (monto * cupon.valor / 100)
            context['total'] = precio(total)
            return JsonResponse(context, status=200)
        except Exception as e:
            print(e)
            return JsonResponse(context, status=404)
@login_required
def pagar(request):
    if request.method == 'POST':
        carro = Carro.objects.filter(user=request.user)
        ctx = {'carro': carro}
        print(request.POST['valor'])
        
        return render(request, 'pago.html', ctx)