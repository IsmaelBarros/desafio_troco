from django.urls import path
from . import views

urlpatterns = [
    path('troco/', views.troco),
    path('lista_detalhes/', views.lista_detalhes),
    path('troco_detalhe/<int:pk>/', views.troco_detalhe)
]
