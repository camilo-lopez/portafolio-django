from django.urls import path
from tarjetas import views

urlpatterns = [
    path('', views.sumar, name='resultado'),
]
