from django.urls import path
from . import views

urlpatterns = [
    path('agregar_carro/<int:id_prod>', views.agregar_carro, name='agregar_carro'),
]
