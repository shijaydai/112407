
import openpyxl
from random import randint
from time import sleep
from fake_useragent import UserAgent
import pandas as pd
import Gapp.models
from .models import dj,store
from django.shortcuts import render, redirect
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests, json
from selenium import webdriver
from selenium.webdriver import Chrome
import numpy as np
import codecs
from openpyxl import Workbook
from django.http import JsonResponse
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from Gapp.models import User
from django.contrib.auth.hashers import make_password

def visitor(request, place_name="None", formatted_address="None"):
    response_data = {}  # 默认的空字典
    print("AAA")
    print(request.GET)
    data = dj.objects.all()
    data1 = store.objects.all()
    # print("aaa" + request.method + "bbb")
    #if request.GET.get("currentText") != None and request.GET.get("currentText") != None :
    print(request.GET)
    if  request.method == "GET" and request.GET.get("currentText") != None :    
        currentText = request.GET.get("currentText")
        addressText = request.GET.get("address")
        if currentText is not None and addressText is not None:
            try:
                print("name" , currentText)
                print("address" , addressText)
                # 查询匹配的dj对象
                matched_store = store.objects.filter(storename=currentText, address=addressText).first()
                matched_dj = dj.objects.filter(storeid_id =  matched_store.storeid).values()
                matched_effsum = dj.objects.filter(storeid_id = matched_store.storeid, effflag=1).count()
                matched_reccnt = dj.objects.filter(storeid_id = matched_store.storeid).count()
                matched_asw = matched_effsum*100 / matched_reccnt
                print(matched_effsum)
                print(matched_reccnt)
                print(matched_asw)
                 # 将QuerySet对象转换为列表
                matched_dj_list = list(matched_dj)

                # 将列表转换为JSON字符串
                json_data = json.dumps(matched_dj_list)
                print(json_data)
                # 构建JSON响应数据
                response_data = {
                    'comment': json_data,
                    'match_asw': matched_asw,
                }
                #print("111" + response_data + "222")
                # 返回JSON响应
                return JsonResponse(response_data)

            except dj.DoesNotExist:
                # 如果没有匹配的记录，返回错误消息和HTTP状态码
                return JsonResponse({'error': 'No matching record found'}, status=404)
        else:
            # 如果缺少必要的参数，返回错误消息和HTTP状态码
            return JsonResponse({'error': 'Missing currentText or address parameter'}, status=400)

    # 如果请求方法不是GET，返回错误响应和HTTP状态码
    # return render(request, "visitor.html",locals())
    
    return render(request, "visitor.html", {'response_data': response_data})

def index(request):
   
    return render(request, "index.html", locals())



def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('passwd')
        password1 = request.POST.get('passwd1')

        # 简单的密码验证，你可以根据需要添加更复杂的验证逻辑
        if password == password1:
            if not User.objects.filter(username=username).exists():
                # 创建User实例并保存到数据库
                user = User.objects.create(email=email, username=username, password=make_password(password))
                user.save()
                # 注册成功后重定向到登录页面
                return redirect('/login')
            else:
                message = "帳號已經存在。"
        else:
            message = "密碼不匹配。"
    else:
        message = ""
    print(message)
    return render(request, 'register.html', {'message': message})

def login(request):
    message = ""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('passwd')
        print(email,password)
        user = authenticate(email=email,password=password)
        print(user)
        if user:
            auth_login(request, user)  # 登录用户
            return redirect('/visitor')  # 登录成功后跳转到会员页面
        else:
            message = "登入失敗，請檢查帳號和密碼是否正確。"
    return render(request, 'login.html', {'message': message})