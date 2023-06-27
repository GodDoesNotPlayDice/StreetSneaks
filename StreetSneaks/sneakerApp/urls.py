from django.urls import path
from . import views

urlpatterns = [
    path('novedades/', views.novedades, name='novedades'),
    path('hombre/', views.hombre, name='hombre'),
    path('mujer/', views.mujer, name='mujer'),
    path('niño/', views.nino, name='niño'),
    path('gestion-zapatillas/', views.sneaks, name='gestion-zapatillas'),
    path('create', views.createSneak, name='createSneak'),
    path('detalle/<str:nombre>/<str:sneak_id>', views.sneak_details, name='sneak_details'),
    path('delete/<int:id>', views.deleteSneak, name='deleteSneak'),
    path('editar/<int:id>', views.editar_zapatilla, name='editar'),
    path('modify/<int:id>', views.editSneak ,name='update'),
    path('vendedores/', views.vendedores, name='vendedores'),
    path('deleteUser/<int:id>', views.deleteUser, name='deleteUser'),
    path('acenderVendedor/<int:id>', views.acenderVendedor, name='acenderVendedor'),
    path('decenderVendedor/<int:id>', views.decenderVendedor, name='decenderVendedor'),
    path('busquedaUser/', views.busquedaUser, name='busquedaUser'),
]
