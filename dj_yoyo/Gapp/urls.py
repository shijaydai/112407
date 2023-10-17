from django.contrib import admin
from django.urls import path
from Gapp import views

urlpatterns = [
    path('visitor/', views.visitor, name='visitor'),
    path('index/', views.index, name='index'),
    # path('login/', views.user_login, name='login'),
    # path('testA/<str:place_name>/<str:formatted_address>/', views.testA, name='testA'),
]