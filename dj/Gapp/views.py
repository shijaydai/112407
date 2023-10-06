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




def testA(request, place_name="None", formatted_address="None"):
    print(request.GET)
    data = dj.objects.all()
    data1 = store.objects.all()
<<<<<<< HEAD
    # print("aaa" + request.method + "bbb")
    #if request.GET.get("currentText") != None and request.GET.get("currentText") != None :
    if  request.method == "GET" and request.GET.get("currentText") != None and request.GET.get("currentText") != None :    
        currentText = request.GET.get("currentText")
        addressText = request.GET.get("address")
    
        if currentText is not None and addressText is not None:
            try:
                print("name" , currentText)
                print("address" , addressText)
                # 查询匹配的dj对象
                #matched_dj = dj.objects.get(
                #matched_store = store.objects.get(
                matched_store = store.objects.filter(storename=currentText, address=addressText).first()
                # if matched_store is None:
                    #storeid =  "1001"
                     #storeid__storename=currentText,
                     #storeid__address=addressText
                    #storename = currentText
                    #"饌味香麵食館", 
                    #currentText,
                    #address="100台灣臺北市中正區濟南路二段6-1號"
                    #"100台灣臺北市中正區濟南路二段6-1號" 
                    #addressText
                #)#.objects.get(address=addressText)
                # print(store.DoesNotExist)
                # if store.DoesNotExist:
                #     return JsonResponse({'error': 'No matching record found in store'}, status=404)
                # print('id',matched_store.storeid)
                # for item in matched_store:
                #     print(item)
                #print("ccc" + aa.+ "222")

                matched_dj = dj.objects.get(
                    storeid =  matched_store.storeid
                     #storeid__storename=currentText,
                     #storeid__address=addressText
                )
                print(matched_dj.username)
                print(matched_dj.msgtime)
                print(matched_dj.star)
                print(matched_dj.comment)
                # 构建JSON响应数据
                response_data = {
                    'username': matched_dj.username,
                    'msgtime': matched_dj.msgtime,
                    'star': matched_dj.star,
                    'comment': matched_dj.comment,
                    'effflag': matched_dj.effflag
                }
                #print("111" + response_data + "222")
                # 返回JSON响应
                return JsonResponse(response_data)
=======
    # data = dj.objects.filter(star = 5) #要用一個條件傳到這裡的r
    if request.method == "GET" and request.GET.get("address") != None:
        print(request.GET)

    try:
        matched_dj = dj.objects.filter(
            storeid__storename=place_name,
            storeid__address=formatted_address
        ).first()
>>>>>>> de7f4e6329e05b3054fbff63ff8dcbb878b8d618

        if matched_dj:
            print("hello")
                # 匹配成功，可以在这里返回匹配的数据或渲染相应的模板
            return render(request, 'test.html', {'item': matched_dj})

<<<<<<< HEAD
    # 如果请求方法不是GET，返回错误响应和HTTP状态码
    # return render(request, "test.html",locals())
    return render(request, "test.html", {'response_data': response_data})
=======
    except dj.DoesNotExist:
            pass

        # 如果没有匹配或发生异常，可以返回一个适当的响应
    return render(request, "test.html",locals())

 
>>>>>>> de7f4e6329e05b3054fbff63ff8dcbb878b8d618
