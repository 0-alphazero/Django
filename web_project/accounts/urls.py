from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),  # homepage view function

    path('products/', views.products ,name='products'),
    path('customer/<str:pk>/', views.customer , name= 'customer'),


]
