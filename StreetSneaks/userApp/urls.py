from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.signin, name='login'),
    path('register/', views.signup, name='register'),
    path('signout', views.signout, name='logout'),
    path('save_direccion', views.save_direccion, name='save_direccion'),
    path('del_direccion<int:id_direccion>', views.del_direccion, name='del_direccion'),
    path('edit_direccion/<int:id_direccion>', views.edit_direccion , name='edit_direccion'),
    path('edi_direct/<int:id_direccion>', views.edi_direct, name='edi_direct'),
    path('editar_profile/', views.goEdit, name='editar_usuario'),
    path('editar_usuario/', views.editarUsuario, name='editUser'),
]
