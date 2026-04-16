from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("account/", views.account, name="account"),
    path("manage/", views.manage, name="manage"),
    path("manage/create_artist", views.create_artist, name="create_artist"),
    path(
        "account-status/<str:account_id>/", views.account_status, name="account_status"
    ),
    path("create-account-link/", views.create_account_link, name="create_account_link"),
]
