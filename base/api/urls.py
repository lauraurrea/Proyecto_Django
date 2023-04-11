from django.urls import path
from . import views

urlpatterns = [
    path('', views.routes),
    path('usuarios/', views.usuarios),
    path('amigos/<str:usuario>', views.amigos),
    path('posts/<str:usuario>', views.posts),
    path('seguir/<str:usuario1>/<str:usuario2>', views.seguir),
]