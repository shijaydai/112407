from django.contrib import admin
from django.urls import path
from Gapp import views

urlpatterns = [
    path('test/<str:place_name>/<str:formatted_address>/', views.test, name='test' ),
    path('display/', views.display_data, name='display_data'),
]