
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('search_result', views.search_result, name='search_result'),
]
