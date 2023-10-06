from django.urls import path
from app_cad_usuarios import views


urlpatterns = [
    # rota, view responsavel, nome referencia
    #usuario.com     
    path('', views.home, name='home' ),
    # usuarios.com/
    path('usuarios/', views.usuario, name='listagem_usuarios')
    
]
