
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

def testA(request, place_name="None", formatted_address="None"):
    response_data = {}  # 默认的空字典
    print("AAA")
    print(request.GET)
    data = dj.objects.all()
    data1 = store.objects.all()
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

            except dj.DoesNotExist:
                # 如果没有匹配的记录，返回错误消息和HTTP状态码
                return JsonResponse({'error': 'No matching record found'}, status=404)
        else:
            # 如果缺少必要的参数，返回错误消息和HTTP状态码
            return JsonResponse({'error': 'Missing currentText or address parameter'}, status=400)

    # 如果请求方法不是GET，返回错误响应和HTTP状态码
    # return render(request, "test.html",locals())
    return render(request, "test.html", {'response_data': response_data})
