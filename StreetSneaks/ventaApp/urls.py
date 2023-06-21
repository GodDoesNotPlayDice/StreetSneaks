from django.urls import path
from . import views

urlpatterns = [
    path('agregar_carro/<int:id_prod>', views.agregar_carro, name='agregar_carro'),
    path('eliminar_carro/<int:carro_id>', views.eliminar_carro, name='eliminar_carro'),
    path('agregar_cupon/', views.agregar_cupon, name='agregar_cupon'),
    path('eliminar_cupon/<int:id_cupon>', views.eliminar_cupon, name='eliminar_cupon'),
    path('api/validar_cupon', views.validar_cupon, name='validar_cupon'),
    path('api/validar_direccion', views.validar_direccion, name='validar_direccion'),
    path('pago/', views.pagar, name='pago'),
    path('pedidos/mis_pedidos/', views.pedidos, name='mis_pedidos'),
    path('confirmacion_pago/<str:fecha_entrega>', views.pagar_confirmar, name='pagando'),
]
