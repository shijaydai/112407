from django.contrib import admin
from django.urls import path
from Gapp import views

urlpatterns = [
    path('visitor/', views.visitor, name='visitor'),
    path('index/', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('feadback/', views.feadback, name='feadback'),
    path('show_favorite_locations/', views.show_favorite_locations, name='show_favorite_locations'),
    path('add_favorite_location/', views.add_favorite_location, name='add_favorite_location'),
    path('unfavorite-location/<int:location_id>/', views.unfavorite_location, name='unfavorite_location'),
    # path('login/', views.user_login, name='login'),
    # path('testA/<str:place_name>/<str:formatted_address>/', views.testA, name='testA'),
]