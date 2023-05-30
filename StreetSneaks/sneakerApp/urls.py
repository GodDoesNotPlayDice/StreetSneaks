from django.urls import path
from . import views

urlpatterns = [
    path('novedades/', views.novedades, name='novedades'),
    path('hombre/', views.hombre, name='hombre'),
    path('mujer/', views.mujer, name='mujer'),
    path('niño/', views.nino, name='niño'),
    path('deportivo/', views.deportivo, name='deportivo'),
    path('gestion-zapatillas/', views.sneaks, name='gestion-zapatillas'),
    path('create', views.createSneak, name='createSneak'),
    path('delete/<int:id>', views.deleteSneak, name='deleteSneak'),

]
