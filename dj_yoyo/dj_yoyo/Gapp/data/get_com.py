import csv
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv
import os
import requests
import re
import json

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path, override=True)  # 設定 override 才會更新變數
GOOGLE_PLACES_API_KEY = os.environ.get("GOOGLE_PLACES_API_KEY")

a_type_list = ['餐廳']

# 取得基本資料json
def get_textsearch(GOOGLE_PLACES_API_KEY, address, a_type):
    URL = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
    response = requests.get(URL + "query=" + f'{address[0]}{address[1]}{a_type}' + '&language=zh-TW' + "&key=" + GOOGLE_PLACES_API_KEY)
    data = response.text  # 使用 .text 屬性取得解碼後的文本

    # 進一步處理 data，如果需要的話
    data = data.replace('"<a href=', '')
    data = re.sub(r'>.*</a>"', '', data)

    # 寫入文件時指定 utf-8 編碼
    with open(os.getcwd() + f'/{address[0]}{address[1]}{a_type}.json', 'w', encoding='utf-8') as f:
        f.write(data)

# 將所有市區路的資料取得
with open('臺北市區路段資料.csv',newline='',encoding='utf-8')as csvfile:
    address_list = list(csv.reader(csvfile))[1:]
    list(address_list)
    # address= ['市區','路']
    #1-10
    address_list
    print(address_list)
    for address in address_list:
        for a_type in a_type_list:
            if f'{address[0]}{address[1]}{a_type}.json' in os.listdir():
                print(f'{address[0]}{address[1]}{a_type}.json','已存在')
            else:
                print('產生',f'{address[0]}{address[1]}{a_type}.json')
                get_textsearch(GOOGLE_PLACES_API_KEY,address,a_type)

            filename = f'{os.getcwd()}/{address[0]}{address[1]}{a_type}.json'