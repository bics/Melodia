
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<str:name>/<int:pk>/<int:artistPK>', views.album, name='album'),
]
