import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
import re
from .models import dj,store,feedback
def get_data(review, storeid):
    # 取得名字
    name_element = review.find_element(By.CLASS_NAME, 'TSUbDb')
    name = name_element.find_element(By.TAG_NAME, 'a').text
    
    # 取得評分
    rating_element = review.find_element(By.CLASS_NAME, 'lTi8oc.z3HNkc')
    rating = rating_element.get_attribute('aria-label').split("：")[1].split(" ")[0]
    
    # 取得日期
    date_element = review.find_element(By.CLASS_NAME, 'dehysf.lTi8oc')
    date = date_element.text
    
    # 取得評論
    comment_element = review.find_element(By.CLASS_NAME, 'Jtu6Td')
    comment = comment_element.text
    
    # 將評論資料存入字典
    dj.objects.create(
        username=name,
        msgtime=date,
        star=int(rating[:1]),
        comment=remove_emojis(comment),
        effflag=1,
        storeid_id=storeid
    )
    review_data = {
        'storeid': storeid,
        'name': name,
        'rating': rating,
        'date': date,
        'comment': remove_emojis(comment),
    }
    print(review_data)
    return review_data

# 現在 review_data_list 中包含了每條評論的資料，你可以進一步處理或存儲這些資料

def remove_emojis(text):
    # 定義正規表達式，匹配表情符號的模式
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # 表情符號 (emoticons)
                               u"\U0001F300-\U0001F5FF"  # 圖形符號 (geometric shapes)
                               u"\U0001F680-\U0001F6FF"  # 交通符號 (transport & map symbols)
                               u"\U0001F700-\U0001F77F"  # 裝置指示符 (alchemical symbols)
                               u"\U0001F780-\U0001F7FF"  # 連結字形標記 (geometric shapes extended)
                               u"\U0001F800-\U0001F8FF"  # 表情符號補充 (supplemental symbols & pictographs)
                               u"\U0001F900-\U0001F9FF"  # 裝置指示符補充 (supplemental symbols & pictographs extended)
                               u"\U0001FA00-\U0001FA6F"  # 裝置指示符補充 (supplemental symbols & pictographs extended-A)
                               u"\U0001FA70-\U0001FAFF"  # 裝置指示符補充 (supplemental symbols & pictographs extended-B)
                               "]+", flags=re.UNICODE)
        # 使用正規表達式將表情符號替換為空字串
    cleaned_text = emoji_pattern.sub(r'', text)
    cleaned_text = cleaned_text.replace('\n', ' ')
    return cleaned_text
# 使用 Chrome 驅動器


def getnew(namelist):
    review_result = []
    driver = webdriver.Chrome()
    # namelist =[ "巧之味手工水餃 濟南店 ","饌味香麵食館 中正"]
    # 1. 在 Google 搜尋列中輸入 "ABC"
    driver.get("https://www.google.com/")
    time.sleep(2)
    for name in namelist:
        if name.id <= 2340:
            continue
        print(name.id,name.storename)
        storeid = name.id
        search_box = driver.find_element(By.NAME, "q")
        search_box.clear()
        search_box.send_keys(f"{name.storename} {name.address}") #搜尋的資料
        search_box.send_keys(Keys.RETURN)
        try:
            # 2. 找到元素中的評論連結並點擊
            review_link = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-async-trigger="reviewDialog"]'))
            )
            review_link.click()

            # 3. 爬取評論頁面中指定 class 的資料
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'WMbnJf'))
            )
                    
            # 等待一些時間以便新的評論載入
            time.sleep(1)
                # 3. 找到 review-dialog-list 元素
            review_list = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'review-dialog-list'))
            ) 

            # 等待最新按钮可点击
            newest_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@data-sort-id='newestFirst']"))
            )

            # 点击最新按钮
            newest_button.click()

            #滑動
            for i in range(10):
                pyautogui.scroll(-100000)
                pyautogui.scroll(-100000)
                time.sleep(0.33)  # 等待一些時間以便新的內容載入

            # 3. 找到並點擊所有 review-more-link 元素
            review_more_links = driver.find_elements(By.CLASS_NAME, 'review-more-link')
            for link in review_more_links:
                # 使用 JavaScript 模擬點擊更多
                driver.execute_script("arguments[0].click();", link)
                
            time.sleep(1)

            # 4. 找到所有的評論
            reviews = driver.find_elements(By.CLASS_NAME, 'WMbnJf')
            for review in reviews:
                review_result.append(get_data(review,storeid))
        except:
            continue
    # 將評論資料列表轉換為 DataFrame
    df = pd.DataFrame(review_result)
    # # 將 DataFrame 寫入 CSV 檔案
    # df.to_csv(f'商家評論.csv', index=False)

    driver.quit()