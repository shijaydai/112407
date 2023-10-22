import json
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

import json
from django.db import models

class store(models.Model):
    storeid = models.IntegerField(primary_key=True)
    storename = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    def __str__(self):
        return self.storeid
    
class dj(models.Model):
    username = models.CharField(max_length=100)
    msgtime = models.CharField(max_length=50)
    star = models.PositiveIntegerField()
    comment = models.CharField(max_length=5000)
    effflag = models.PositiveIntegerField()
    storeid = models.ForeignKey(store, on_delete=models.CASCADE)
     
class effective(models.Model):
    storeid = models.IntegerField(primary_key=True)
    eff = models.CharField(max_length=10)
    noeff = models.CharField(max_length=10)

    
class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255, blank=False, null=False)
    # # 設置 related_name 參數
    # groups = models.ManyToManyField(Group, related_name='customuser_set')
    # user_permissions = models.ManyToManyField(Permission, related_name='customuser_set')
    USERNAME_FIELD = "email"  # 使用信箱當登入帳號
    REQUIRED_FIELDS = ["username"]  # username 是預設的必填欄位
    def __str__(self):
        return self.username