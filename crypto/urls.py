from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('prices', views.prices, name='prices'),
    path('top_crypto', views.top_crypto, name='top_crypto')
]