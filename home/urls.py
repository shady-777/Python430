from .views import *
from django.urls import path

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name="about"),
    path('contact', contact, name="contact"),
    path('price', price, name="price"),
    path('portfolio', portfolio, name="portfolio"),
    path('services', services, name="services"),
]
