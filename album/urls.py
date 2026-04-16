from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path(
        "<str:name>/<int:pk>/<int:artistPK>/edit", views.edit_album, name="edit_album"
    ),
    path(
        "<str:name>/<int:pk>/<int:artistPK>/create_track",
        views.create_track,
        name="create_track",
    ),
]
