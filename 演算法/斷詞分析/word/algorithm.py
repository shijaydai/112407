import pandas as pd
import numpy as np
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('vader_lexicon')
nltk.download('stopwords')
nltk.download('punkt')

# 讀取 CSV 檔
data = pd.read_csv('Gappdj_segmented_no_test25.csv', encoding='cp950')

# 初始化情感分析器
sia = SentimentIntensityAnalyzer()

# 移除停用詞
stop_words = set(stopwords.words('chinese'))  # 修改 'chinese' 為你使用的語言
def remove_stopwords(text):
    if pd.isnull(text) or ('|' in text) or ('/' in text) or ('\\' in text):
        return '1'  # 如果是空值、包含 '|'、'/' 或 '\'，回傳 '1'
    return text

# 增加情感分析分數至 DataFrame
data['compound'] = data['segmented'].apply(lambda x: sia.polarity_scores(remove_stopwords(x))['compound'])

# 設定情感分析分數閾值，任何情感分數不為0的都視為有情感
data['is_positive'] = np.where(data['compound'] != 0, 0, 1)

# 處理特殊情況：有出現 \ / | 且字數低於55的強制顯示為1
data['is_positive'] = np.where((data['is_positive'] == 0) & (data['segmented'].str.contains('[\\/|]')) & (data['segmented'].str.len() < 55), 1, data['is_positive'])

# 修正is_positive的部分，處理空值
data['is_positive'] = np.where((pd.isnull(data['segmented']) | (data['segmented'].str.strip() == '')), 1, data['is_positive'])

# 計算每家店的有效評論占比
store_effectiveness = data.groupby(['id', 'segmented'])[['is_positive']].mean().reset_index()

# 匯出至 CSV 檔案
store_effectiveness.to_csv('segmented_no_test25.csv', index=False, encoding='cp950')
