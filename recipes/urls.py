from django.contrib import admin
from django.urls import path
from recipes.views import sobre, home

urlpatterns = [
    path('', home),
    path('sobre/', sobre),

]
