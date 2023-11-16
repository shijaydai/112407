from django.contrib import admin
from Gapp import models
from django.contrib.auth.admin import UserAdmin
admin.site.register(models.User,UserAdmin)
admin.site.register(models.dj)
admin.site.register(models.store)
