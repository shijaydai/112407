import os
from django.conf import settings
from django.urls import include, path
from Gapp.views import visitor
from django.conf.urls.static import static
from dj.settings import BASE_DIR
from django.contrib import admin
from Gapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('visitor/',visitor),
    # path('visitor/', views.visitor_view, name='visitor_page'),
    
    path('index/', views.index, name='index'),
    path('', views.index),
#     path('login/',login)
]

