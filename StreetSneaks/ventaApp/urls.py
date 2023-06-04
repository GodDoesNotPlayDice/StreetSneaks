from django.urls import path
from . import views

urlpatterns = [
    path('agregar_carro/<int:id_prod>', views.agregar_carro, name='agregar_carro'),
    path('eliminar_carro/<int:carro_id>', views.eliminar_carro, name='eliminar_carro'),
    path('agregar_cupon/', views.agregar_cupon, name='agregar_cupon'),
    path('eliminar_cupon/<int:id_cupon>', views.eliminar_cupon, name='eliminar_cupon'),
    path('api/validar_cupon', views.validar_cupon, name='validar_cupon'),
]
