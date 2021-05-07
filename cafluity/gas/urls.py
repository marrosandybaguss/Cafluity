from django.urls import path

from . import views

urlpatterns = [
    path('', views.real_gas, name='index_real_gas'),
    path('real-gas/', views.real_gas, name='real_gas'),
]