from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.signin, name='login'),
    path('register/', views.signup, name='register'),
    path('signout', views.signout, name='logout'),
    path('save_direccion', views.save_direccion, name='save_direccion'),
    path('del_direccion<int:id_direccion>', views.del_direccion, name='del_direccion')
]
