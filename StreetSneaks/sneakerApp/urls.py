from django.urls import path
from . import views

urlpatterns = [
    path('novedades/', views.novedades, name='novedades'),
    path('hombre/', views.hombre, name='hombre'),
    path('mujer/', views.mujer, name='mujer'),
    path('niño/', views.nino, name='niño'),
    path('gestion-zapatillas/', views.sneaks, name='gestion-zapatillas'),
    path('create', views.createSneak, name='createSneak'),
    path('delete/<int:id>', views.deleteSneak, name='deleteSneak'),
    path('<str:nombre>/<str:sneak_id>', views.sneak_details, name='sneak_details'),
]
