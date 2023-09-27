from django.contrib import admin
from django.urls import path
from Gapp import views

urlpatterns = [
    path('testA/', views.testA, name='testA'),
]