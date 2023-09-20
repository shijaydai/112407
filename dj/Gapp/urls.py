from django.contrib import admin
from django.urls import path
from Gapp import views

urlpatterns = [


    
    # path('', views.index,name='index'),
    # path('login/', views.login ),
    # path('result/',result),
    # path('index/grouping/',grouping),
    # path('index/reply/',reply),
    path('test/', views.test ),

]