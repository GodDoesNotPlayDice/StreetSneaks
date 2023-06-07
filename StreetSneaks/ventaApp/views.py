from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.http import JsonResponse
from userApp.models import Direccion
from sneakerApp.models import Zapatilla
from userApp.models import Carro
from .models import Cupon, Iva
from mainApp.templatetags.filters import precio
from datetime import datetime, timedelta
import locale


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
            carro = Carro.objects.filter(user=request.user)
            monto = 0
            cupon = Cupon.objects.get(name=cuponText)
            print(cupon.name)
            for c in carro:
                monto += c.items.precio
                c.cupon = cupon
                c.save()
            total = monto - (monto * cupon.valor / 100)
            context['total'] = precio(total)
            return JsonResponse(context, status=200)
        except Exception as e:
            print(e)
            for c in carro:
                c.cupon = None
                c.save()
            return JsonResponse(status=404) 
        
@login_required
def validar_direccion(request):
    ctx = {}  # Declarar el diccionario ctx fuera del bloque try

    try:
        if request.method == 'POST':
            direccion_id = request.POST.get('direccion')
            direccion = get_object_or_404(Direccion, id=direccion_id, user=request.user)
            carros = Carro.objects.filter(user=request.user)
            for carro in carros:
                carro.direccion = direccion
                carro.save()
            ctx['direccion'] = str(direccion.direccion) 
            return JsonResponse(ctx, status=200)
    except Exception as e:
        print(e)
        carros = Carro.objects.filter(user=request.user)
        for carro in carros:
            carro.direccion = None
            carro.save()
    ctx['error'] = 'Error al validar la dirección'
    return JsonResponse(ctx, status=404)

@login_required
def pagar(request):
    iva = Iva.objects.get(id=1).valor
    locale.setlocale(locale.LC_ALL, 'es_ES.utf8')
    fecha_actual = datetime.now().date()
    fecha_nueva = fecha_actual + timedelta(days=3)
    fecha_formateada = fecha_nueva.strftime('%d de %B del %Y')
    carro = Carro.objects.filter(user=request.user)
    items = [c.items for c in carro]
    total = sum(item.precio for item in items)
    cupon = [c.cupon for c in carro]
    try:
        cupon_valores = sum([c.cupon.valor for c in carro])
        for i in cupon:
            cupon_nombre = i.name
    except:
        cupon_valores = 0
        cupon_nombre = "No hay"
    descuento = int(total * cupon_valores / 100)
    direccion = [c.direccion for c in carro]
    total_con_descuento = total - descuento
    total_con_iva = total_con_descuento + (total_con_descuento * iva / 100)
    
    ctx = {
        'items': items,
        'cupon': cupon,
        'cupon_nombre': cupon_nombre,
        'direccion': direccion,
        'fecha': fecha_formateada,
        'descuento': descuento,
        'iva': iva,
        'total': int(total_con_iva)
    }
    
    return render(request, 'pago.html', ctx)