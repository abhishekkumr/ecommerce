from django.contrib import admin
from django.urls import path,include
from .views import ecom  


#this is the main url from which we can access the DjangoRestFramwork dashboard.
urlpatterns = [
    path('home/', ecom),
]