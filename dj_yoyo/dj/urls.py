import os
from django.conf import settings
from django.urls import include, path
from Gapp.views import visitor,member
from django.conf.urls.static import static
from dj.settings import BASE_DIR
from django.contrib import admin
from Gapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('visitor/',visitor),
    path('member/',member),
    path('index/', views.index, name='index'),
    path('', views.index),
    path('register/', views.register, name='register'),
    path('login/',views.login, name='login'),
    path('feadback/', views.feadback, name='feadback'),
    path('test/', views.test),
    path('show_favorite_locations/', views.show_favorite_locations, name='show_favorite_locations'),
    path('add_favorite_location/', views.add_favorite_location, name='add_favorite_location'),
    path('unfavorite-location/<int:location_id>/', views.unfavorite_location, name='unfavorite_location'),
    path('change_password/', views.change_password, name='change_password'),
    path('searchhistory/', views.searchhistory, name='searchhistory'),
]

