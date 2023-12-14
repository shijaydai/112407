import pandas as pd
import os
import re
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

# 讀取CSV檔案
spam_dataframe = pd.read_csv('/Users/Lenovo/Desktop/word/Gappdj_en.csv', encoding='utf-8')

# 使用CountVectorizer將文本數據轉換為詞袋模型矩陣
vectorizer = CountVectorizer()
spamham_countVectorizer = vectorizer.fit_transform(spam_dataframe['text'])

# 拆分數據為訓練集和測試集
X = spamham_countVectorizer
y = spam_dataframe['effflag']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 使用scikit-learn的Naive Bayes分類器進行訓練
NB_classifier = MultinomialNB()
NB_classifier.fit(X_train, y_train)

# 在測試集上進行預測並打印分類報告
y_predict_test = NB_classifier.predict(X_test)
print("整體分類報告:")
print(classification_report(y_test, y_predict_test))

# 預處理文本數據的函式
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    tokens = text.split()
    return ' '.join(tokens)

# 建立 storeid 對應店家的字典
store_dict = {}
for index, row in spam_dataframe.iterrows():
    store_id = row['storeid']
    if store_id not in store_dict:
        store_dict[store_id] = []
    store_dict[store_id].append(index)

# 遍歷店家字典，針對每一間店家進行分析
for store_id, indices in store_dict.items():
    print(f"\n分析店家 {store_id}:")

    # 提取該店家的文本和標籤
    store_texts = [preprocess_text(spam_dataframe.loc[i, 'text']) for i in indices]
    store_labels = spam_dataframe.loc[indices, 'effflag']

    # 使用CountVectorizer轉換文本
    store_vectorizer = CountVectorizer()
    store_X = store_vectorizer.fit_transform(store_texts)

    # 使用 scikit-learn 的 Naive Bayes 分類器進行訓練
    store_NB_classifier = MultinomialNB()
    store_NB_classifier.fit(store_X, store_labels)

    # 預測每條評論的有效性，並將結果存儲到 'effflag_prediction' 欄位
    spam_dataframe.loc[indices, 'effflag_prediction'] = store_NB_classifier.predict(store_X)

    # 打印店家內的分類報告
    store_y_predict_test = store_NB_classifier.predict(store_X)
    print(f"店家 {store_id} 內的分類報告:")
    print(classification_report(store_labels, store_y_predict_test))

# 將結果存儲為 CSV 檔案
spam_dataframe.to_csv('/Users/Lenovo/Desktop/word/Gappdj_en_predictions.csv', index=False, encoding='utf-8-sig')
