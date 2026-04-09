
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<str:name>/<int:pk>/donate', views.donate, name='donate'),
    path('payment_successful/', views.payment_success, name='payment_success'),
    path('webhook/', views.stripe_webhook, name='stripe_webhook'),
]
