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
    # data = dj.objects.filter(star = 5) #要用一個條件傳到這裡的r
    if request.method == "GET" and request.GET.get("address") != None:
        print(request.GET)

    try:
        matched_dj = dj.objects.filter(
            storeid__storename=place_name,
            storeid__address=formatted_address
        ).first()

        if matched_dj:
            print("hello")
                # 匹配成功，可以在这里返回匹配的数据或渲染相应的模板
            return render(request, 'test.html', {'item': matched_dj})

    except dj.DoesNotExist:
            pass

        # 如果没有匹配或发生异常，可以返回一个适当的响应
    return render(request, "test.html",locals())

 
