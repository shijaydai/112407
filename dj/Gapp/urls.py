from django.contrib import admin
from django.urls import path
from Gapp import views

urlpatterns = [
    # path('testA/', views.testA, name='testA'),
    path('testA/<str:place_name>/<str:formatted_address>/', views.testA, name='testA'),
]