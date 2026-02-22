
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.members, name='members'),
    path('favourites/', views.favourites, name='favourites'),
    path('account/', views.account, name='account'),
    path('manage/', views.manage, name='manage'),
    path('manage/create_artist', views.create_artist, name='create_artist'),

]
