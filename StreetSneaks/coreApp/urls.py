from django.urls import path
from . import views

urlpatterns = [
    path('trabaja-con-nosotros/', views.work, name='work'),
    path('privacidad/', views.priv, name='priv'),
    path('preguntas-frecuentes/', views.faq, name='faq'),
    path('Terminos-y-Servicio/', views.tos, name='tos'),
]
