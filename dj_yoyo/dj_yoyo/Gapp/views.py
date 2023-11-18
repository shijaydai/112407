
import csv
import os
import openpyxl
from random import randint
from time import sleep
from fake_useragent import UserAgent
import pandas as pd
import Gapp.models
from .models import dj,store,feedback,FavoriteLocation
from django.shortcuts import render, redirect, get_object_or_404
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
from django.http import HttpResponseRedirect
import logging
from .get_new import getnew

def visitor(request, place_name="None", formatted_address="None"):
    response_data = {}  # 默认的空字典
    print("AAA")
    print(request.GET)
    data = dj.objects.all()
    data1 = store.objects.all()
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

                if matched_store is not None:
                    matched_dj = dj.objects.filter(storeid_id=matched_store.id).values()
                
                 # 将QuerySet对象转换为列表
                matched_dj_list = list(matched_dj)

                # 将列表转换为JSON字符串
                json_data = json.dumps(matched_dj_list)
                print(json_data)
                # 构建JSON响应数据
                response_data = {
                    'comment': json_data,
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

def member(request, place_name="None", formatted_address="None"):
    response_data = {}  # 默认的空字典
    data = dj.objects.all()
    data1 = store.objects.all()
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

                if matched_store is not None:
                    matched_dj = dj.objects.filter(storeid_id=matched_store.id).values()
                    matched_effsum = dj.objects.filter(storeid_id=matched_store.id, effflag=1).count()
                    matched_reccnt = dj.objects.filter(storeid_id=matched_store.id).count()
                    matched_asw = matched_effsum * 100 / matched_reccnt if matched_reccnt != 0 else 0

                    matched_dj_list = list(matched_dj)
                    json_data = json.dumps(matched_dj_list)

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

    # ---------------------------------------------------收藏功能
    if request.method == "POST" and request.POST.get("currentText") != None : 
        # placename = request.POST.get('currentText')
        # placeaddress = request.POST.get('address')
        currentText = request.POST.get("currentText")
        addressText = request.POST.get("address")
        logging.info(f"Received a POST request with placename: {currentText}, placeaddress: {addressText}")
        # 将数据存储到数据库
        favorite_location = FavoriteLocation.objects.create(placename=currentText, placeaddress=addressText)
        favorite_location.save()   
    # 如果请求方法不是GET，返回错误响应和HTTP状态码
    # return render(request, "visitor.html",locals())
    return render(request, "member.html", {'response_data': response_data})

def add_favorite_location(request):
    if request.method == 'POST':
        # 使用request.POST.get()方法获取POST参数
        placename = request.POST.get('currentText')
        placeaddress = request.POST.get('address')
        if not FavoriteLocation.objects.filter(placename=placename, placeaddress=placeaddress).exists():
            # 如果不存在相同数据，则将数据存储到数据库
            favorite_location = FavoriteLocation.objects.create(placename=placename, placeaddress=placeaddress)
            favorite_location.save()
            return JsonResponse({'message': '地址已收藏'})
        else:
            return JsonResponse({'message': '地址已存在'})
    return JsonResponse({'message': '无效的请求'})

def show_favorite_locations(request):
    show_favorite_locations = FavoriteLocation.objects.all()
    if request.method == 'POST': 
        searchvalue = request.POST.get('searchForm')
        return render(request,'member.html' , {'searchvalue': searchvalue} )
    return render(request, 'show_favorite_locations.html',{'show_favorite_locations': show_favorite_locations})

def unfavorite_location(request, location_id):
    location = get_object_or_404(FavoriteLocation, pk=location_id)
    if request.method == 'POST':
        location.delete()
        return redirect('show_favorite_locations')
    return render(request, 'unfavorite_location_confirm.html', {'location': location})


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
                return redirect('login')
            else:
                message = "帳號已經存在。"
        else:
            message = "密碼不匹配。"
            return render(request, 'login.html', {'message': message})
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
            return redirect('/member')  # 登录成功后跳转到会员页面
        else:
            message = "登入失敗，請檢查帳號和密碼是否正確。"
    return render(request, 'login.html', {'message': message})

def feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        feadback = request.POST.get('feadback')
        recommend = request.POST.get('recommend')
        unit = feedback.objects.create(name=name, email=email, feadback=feadback, recommend=recommend)
        unit.save()
        return HttpResponseRedirect('/index/')
    return render(request, "feadback.html", locals())

def extract_name_and_address(json_data):
    lst = []
    results = json_data.get('results', [])
    for result in results:
        name = result.get('name', 'N/A')
        address = result.get('formatted_address', 'N/A')
        lst.append([name,address])
        # print(f"店家名稱: {name}")
        # print(f"地址: {address}")
        # print("------")
    return lst

def process_folder(folder_path):
    all_results = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            print(filename)
            file_path = os.path.join(folder_path, filename)
            with open(file_path, encoding='utf-8') as file:
                json_data = json.load(file)
                lst = extract_name_and_address(json_data)
                all_results.append(lst)
                print(lst)
    return all_results

# def inputsql(request):
#     data_folder_path = os.getcwd()+"\\Gapp\\data\\"
#     all_results = process_folder(data_folder_path)
#     print(len(all_results))
#     for datalst in all_results:
#         for data in datalst:
#             store.objects.create(
#                 storename=data[0],
#                 address=data[1],
#             )
#     return render(request,"test.html",locals())

# def test(request):
#     namelist = store.objects.all()
#     getnew(namelist)
#     # getnew(namelist)
#     return render(request,"test.html",locals())
def check_file_in_folder(folder_path, file_name):
    file_path = os.path.join(folder_path, file_name)
    return os.path.exists(file_path)

def test(request):
    # 使用 values 方法擷取所有欄位
    all_place_list = store.objects.all().values()
    # 將 QuerySet 轉換為列表
    all_place_list_dict = list(all_place_list)
    all_place_list = [x["storename"] for x in  all_place_list ]
    # print(all_place_list)
    # 取得檔案的絕對路徑
    file_path = os.path.join(os.path.dirname(__file__), 'data', '臺北市區路段資料.csv')
    # print(all_place_list,file_path)
    # 呼叫 get_photo 函數並傳遞路徑
    get_photo(all_place_list, file_path)
    return render(request, "test.html", {'all_place_list': all_place_list})



def get_photo(all_place_list, file_path):
    count =0
    with open(file_path, newline="", encoding="utf-8") as csvfile:
        address_list = list(csv.reader(csvfile))
        list(address_list)   
        for address in address_list[1:]:
            with open(f"{os.getcwd()}\\Gapp\\data\\{address[0]}{address[1]}餐廳.json", encoding="utf-8") as file:
                data_opening_phone = json.load(file)
                for data in data_opening_phone["results"]:
                    place_id = data["name"]
                    try:
                        photo_list = data["photos"]
                        if place_id in all_place_list:
                            print(place_id)
                            for num in range(len(photo_list)):
                                if check_file_in_folder(f'{os.getcwd()}\\照片\\備份\\',f'{place_id}.jpg'): continue
                                photo_reference = photo_list[num]["photo_reference"]
                                # print(photo_list[num]["photo_reference"])
                                # print(f'{os.getcwd()}\\照片\\{place_id}_{num+1}.jpg')
                                count+=1
                                # ------------------------------------------------------------------
                                max_width = 1024  # 设置所需的最大宽度
                                max_height = 1024  # 设置所需的最大高度
                                # 构建请求URL，包括maxwidth和maxheight参数
                                # print(data["result"]["name"])
                                url = f"https://maps.googleapis.com/maps/api/place/photo?photoreference={photo_reference}&maxwidth={max_width}&maxheight={max_height}&key=AIzaSyA5KrfTVdXU8zFiOnlFNg763FYvXirAuhU&libraries"
                                # 将your_api_key替换为您的实际API密钥
                                # print(photo_reference)
                                # # 发送HTTP请求获取照片
                                response = requests.get(url)
                                
                                # 将照片保存到文件
                                with open(f'{os.getcwd()}\\照片\\備份\\{place_id}.jpg', "wb") as file:
                                        file.write(response.content) 
                                # all_place_list.remove(place_id)    
                    except Exception as e:
                        print(f"發生未處理的異常: {e}")

