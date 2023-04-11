from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registerPage),
    path('login/', views.loginPage),
    path('logout/',views.logoutPage),

    path('', views.home),

    path('perfil/', views.perfilPage),
    path('publicar/', views.publicacion),
    path('comment/', views.comentar),
    path('megusta/', views.megusta),

    path('amigos/', views.amigos),
    path('seguir/', views.seguir),
    path('eliminar/', views.eliminar),

    path('soporte/', views.soportePage),
]