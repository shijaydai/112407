import os
from django.conf import settings
from django.urls import include, path
from Gapp.views import login,result,index,grouping,reply,Message,Mess,search,react,test
from django.conf.urls.static import static
from dj.settings import BASE_DIR
from django.contrib import admin



urlpatterns = [
    #path('Gapp/', include('Gapp.urls')),
    path('admin/', admin.site.urls),
    path('index/',index),
    path('index/login/', login ),
    path('index/login/result/',result),
    path('index/login/result/grouping/',grouping),
    path('index/login/result/grouping/reply/',reply),
    path('search/react',react),
    path('search/',search),
    path('test/',test)
]

