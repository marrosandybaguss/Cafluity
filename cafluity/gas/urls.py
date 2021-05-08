from django.urls import path

from . import views

urlpatterns = [
    path('', views.real_gas, name='index_real_gas'),
    path('real-gas/', views.real_gas, name='real_gas'),
    path('ideal-gas/', views.ideal_gas, name='ideal_gas'),
]