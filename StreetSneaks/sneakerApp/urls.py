from django.urls import path
from . import views

urlpatterns = [
    path('novedades/', views.novedades, name='novedades'),
    path('hombre/', views.hombre, name='hombre'),
    path('mujer/', views.mujer, name='mujer'),
    path('niño/', views.nino, name='niño'),
    path('deportivo/', views.deportivo, name='deportivo'),
]
