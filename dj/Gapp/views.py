import openpyxl
from random import randint
from time import sleep
from fake_useragent import UserAgent
import pandas as pd
import Gapp.models
from Gapp.models import Mes,Adress,ShopInformation
from django.shortcuts import render, redirect
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests, json
from selenium import webdriver
from selenium.webdriver import Chrome
import numpy as np
import codecs
from openpyxl import Workbook



def login(request):
    return render(request,'login.html',locals())

def result(request):
    return render(request,'result.html',locals())
def index(request):
    return render(request,'index.html',locals())
    #response = redirect('/index')
    #return render(request,'index.html',locals())
def grouping(request):
    return render(request,'grouping.html',locals())
def reply(request):
    return render(request,'reply.html',locals())


def test(request):
        
    return render(request, "test.html", locals())



def search(request):
        
    

    return render(request, "search.html", locals())


def react(request):
    if request.method == "POST":
        ShopName  = request.POST["ShopName"]

    try:
        A = Mes.objects.get(Shop_Name=ShopName)
    except:
        errormessage = "(找不到此店家)"
   

    driver = webdriver.Firefox()  #透過Browser Driver 開啟 Chrome
    default_url = "https://www.google.com/maps/place?q="+str(ShopName)
    driver.get(default_url)

    places = tuple(str(ShopName).split('\n'))
    URL = []
    for i in places:
        URL.append("https://www.google.com/maps/place?q=" + i)
    


    def STR_to_NUM(data):
        line = tuple(data.split(',')) #註1
        num1 = float(line[1])
        num2 = float(line[2])
        line = [num1, num2]
        return line

    # wb = Workbook()
    # ws = wb.active
    # ws['A1'] = 'longitude'
    # ws['B1'] = 'latitude'

    response = requests.get(URL[0])
    soup = BeautifulSoup(response.text, "html.parser")
    text = soup.prettify()
    initial_pos = text.find(";window.APP_INITIALIZATION_STATE")
    #尋找;window.APP_INITIALIZATION_STATE所在位置
    data = text[initial_pos+36:initial_pos+85] #將其後的參數進行存取
    num_data = STR_to_NUM(data)
    
    longitude = num_data[0]
    latitude = num_data[1]
    unit = Adress.objects.create(longitude = longitude , latitude = latitude, AdressName = ShopName)
    unit.save()

    return render(request, "react.html", locals())





    
    


def Mess(request):
    reviews = Mes.objects.all()  #讀取資料表, 依 id 遞增排序
    return render(request, "test.html", locals())



def Message(request):


    A = '雙月'
    all_reviews = ['隊伍永遠那麼長，可是值得等候！食物太美味了而且價錢實惠！員工服務超棒超專業，美中不足的是位子有點少。強推蠔和剝皮椒雞湯。餐點：5服務：5氣氛：3' ,
                    '餐點十分好吃，有一定的水準；店員也很親切，現場吃需要等待時間，外帶建議可以先線上點餐後前往領取，非常方便。' ,
                    '雖然位置不多，但是店員都很親切的招待也於等待時送上茶水。這次吃了經典蛤蜊雞腿跟愛恨椒芝麵。湯鮮甜，麵有彈性不軟爛，但也不會太乾。實至名歸。建議的餐點蛤蜊燉雞湯 愛恨椒芝麵'
                    ]   
    Mes_Percent = "70%"
    Mes_Stars = "****"
    Mes_Suspicious = [
        "值得等候","位置不多","超棒超專業","餐點：5服務：5氣氛：3"
    ]

    unit = Mes.objects.create(Shop_Name = A, Mes_Percent = Mes_Percent, Mes_Stars=Mes_Stars, Mes_Suspicious=Mes_Suspicious) 
    unit.save()  #寫入資料庫

        
    return render(request, "search.html", locals())







    

    
    # 獲取網頁原始碼
    # soup = BeautifulSoup(driver.page_source,"lxml")
    # 獲取評論資料框架
    # all_reviews = soup.find_all(class_ = 'wiI7pd')
    # 以第一則評論為例
    # ar = all_reviews[0]
    #ar.append(all_reviews) # 第幾則評論
    # text_review = ar.find(class_ = "wiI7pd").text
    #ar = all_reviews.split('<span class="wiI7pd">')

    # 評論星數
    # star_review = str(ar.find(class_ = "kvMYJc").get('aria-label').strip().strip("顆星"))
    
    # 評論內容
    # text_review = ar.find(class_ = "wiI7pd").text
    # return render(request,'test.html',locals())
    







#     ua = UserAgent()
#     user_agent = ua.random
#     headers = {
#         'user-agent':user_agent
#     }

#     comments =[]

#     counter = 0
#     while 1:
#         url = "https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765758567264202137!2y15848805525573025855!2m1!1i"+str(counter)+"!3e1!4m6!3b1!4b1!5b1!6b1!7b1!20b1!5m2!1sthF5ZKPOLMvr-Qal0a3YDw!7e81"
#         #url = "https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&authuser=0&pb=!1m2!1y3765758754043517363!2y3994203237871290989!2m2!2i10!3sCAESBkVnSUlDZw%3D%3D!3e1!4m5!3b1!4b1!6b1!7b1!20b1!5m2!1so6iyZJ-DM6_P1e8P9_CMgAM!7e81"
 
#         counter = counter + 10
#         sleep(randint(0,2))
#         text = requests.get(url,headers=headers).text
#         pretext = ')]}\''
#         text = text.replace(pretext,'')
#         soup = json.loads(text)
        

#         conlist = soup[2]
#         if conlist is None:
#             break
        
#         for i in conlist:
#             allcomments = {}
#             allcomments['username'] = tuple(str(i[0][1]))
#             allcomments['time'] = tuple(str(i[1]))
#             allcomments['star'] = tuple(str(i[4]))
#             allcomments['comment'] = tuple(str(i[3]))
#             comments.append(allcomments)
#     df1 = pd.DataFrame(comments)
#     return render(request, 'test.html',locals())


    # url = 'https://www.google.com'
    # res = requests.get(url)
    # soup = BeautifulSoup(res.text, "html.parser")

    # Mes = soup.find_all('div')
    # for M in Mes:
    #     p = M.string

    # return render(request, 'test.html',locals())




