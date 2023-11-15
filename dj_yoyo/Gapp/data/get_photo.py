import psycopg2
from sqltool import Postgres
import os
import csv
import json
import requests

from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path, override=True)  # 設定 override 才會更新變數
GOOGLE_PLACES_API_KEY = os.environ.get("GOOGLE_PLACES_API_KEY")


def check_file_in_folder(folder_path, file_name):
    file_path = os.path.join(folder_path, file_name)
    return os.path.exists(file_path)
