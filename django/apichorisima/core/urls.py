from django.urls import path
from core.views import lista_usuarios, autenticar_usuario
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('usuarios/', lista_usuarios, name='lista_usuarios'),
    path('autenticar/', autenticar_usuario, name='autenticar_usuario'),
]