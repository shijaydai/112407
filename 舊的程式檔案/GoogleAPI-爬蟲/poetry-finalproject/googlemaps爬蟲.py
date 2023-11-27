#引入函式庫
import requests 
import json
from dotenv import load_dotenv, find_dotenv

import googlemaps
import os

from os.path import join, dirname


dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path, override=True)  # 設定 override 才會更新變數哦！

GOOGLE_PLACES_API_KEY = os.environ.get("GOOGLE_PLACES_API_KEY")
print(GOOGLE_PLACES_API_KEY)
# Client
gmaps = googlemaps.Client(key=GOOGLE_PLACES_API_KEY)

# 要查詢的位置坐標（緯度和經度）
location = '25.041935223069615, 121.52558526073895' #'LATITUDE,LONGITUDE'

# 查詢附近的餐廳
radius = 1000  # 半徑，以米為單位
type = 'restaurant'  # 可以更改為其他類型，例如：'cafe', 'hotel', 'gym', 等等

# 發送 API 請求
url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&type={type}&key={GOOGLE_PLACES_API_KEY}'
response = requests.get(url)

# 處理 API 回應
data = response.json()
if data.get('status') == 'OK':
    results = data['results']
    for place in results:
        name = place['name']
        address = place['vicinity']
        print(f'Name: {name}, Address: {address}')
else:
    print('查詢失敗')