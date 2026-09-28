from django.urls import path
from .views import home, validar_estoque


urlpatterns = [
    path('', home, name='home'),
    path('api/validar-estoque/', validar_estoque, name='validar_estoque'),
]