from django.urls import path
from . import views

app_name = 'veiculos'

urlpatterns = [
    path('', views.automovel_lista, name='automovel_lista'),
    path('novo/', views.automovel_criar, name='automovel_criar'),
    path('<int:pk>/', views.automovel_detalhe, name='automovel_detalhe'),
]