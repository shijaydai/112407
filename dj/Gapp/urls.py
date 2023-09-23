from django.contrib import admin
from django.urls import path
from Gapp import views

urlpatterns = [
    path('test/', views.test ),
    path('display/', views.display_data, name='display_data'),
]