from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('prices', views.prices, name='prices'),
    path('top_crypto', views.top_crypto, name='top_crypto'),
    path('top_crypto_2', views.top_crypto_2, name='top_crypto_2'),
    path('top_crypto_3', views.top_crypto_3, name='top_crypto_3'),
]
