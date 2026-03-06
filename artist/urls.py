
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<str:name>/<int:pk>', views.artist, name='artist'),
    path('<str:name>/<int:pk>/create_album', views.create_album, name='create_album'),
]
