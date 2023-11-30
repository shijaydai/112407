import json
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
import json
from django.db import models
from django import forms

class store(models.Model):
    storename = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    
class dj(models.Model):
    username = models.CharField(max_length=255)
    msgtime = models.CharField(max_length=255)
    star = models.PositiveIntegerField()
    comment = models.CharField(max_length=5000)
    effflag = models.PositiveIntegerField()
    storeid = models.ForeignKey(to=store, on_delete=models.CASCADE)
    
class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255, blank=False, null=False)
    # # 設置 related_name 參數
    # groups = models.ManyToManyField(Group, related_name='customuser_set')
    # user_permissions = models.ManyToManyField(Permission, related_name='customuser_set')
    USERNAME_FIELD = "email"  # 使用信箱當登入帳號
    REQUIRED_FIELDS = ["username"]  # username 是預設的必填欄位
    def __str__(self):
        return self.username

class favoritelocation(models.Model):
    placename = models.CharField(max_length=300, default='placename')
    placeaddress = models.CharField(max_length=300, default='placeaddress')
    # placenumber = models.CharField(max_length=300)
    def __str__(self):
        return self.placename

class feedback(models.Model):
    email = models.EmailField(unique=True, max_length=255, blank=False, null=False)
    name = models.CharField(max_length=100)
    feedback = models.CharField(max_length=300)
    recommend = models.CharField(max_length=300)
    def __str__(self):
        return self.name

class ChangePasswordForm(forms.Form):
    new_password = forms.CharField(label='新密碼', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='確認新密碼', widget=forms.PasswordInput)
    new_username = forms.CharField(label='新使用者名稱')

