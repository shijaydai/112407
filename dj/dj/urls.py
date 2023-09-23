import os
from django.conf import settings
from django.urls import include, path
from Gapp.views import test
from django.conf.urls.static import static
from dj.settings import BASE_DIR
from django.contrib import admin



urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/',test)
]

