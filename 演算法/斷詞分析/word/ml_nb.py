import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# 讀取 CSV 檔案
file_path = 'Gappdj_finish.csv'
df = pd.read_csv(file_path, encoding='cp950')

# 處理 NaN 值，這裡使用空字符串代替 NaN
df['segmented'].fillna('', inplace=True)

# 假設 CSV 包含 'text' 欄位、 'storeid' 欄位和 'label' 欄位，其中 'text' 是評論文本，'storeid' 是店家ID，'label' 是標籤（0 或 1）
# 這裡需要根據實際情況修改欄位名稱
X = df['segmented']
y = df['effflag']
store_ids = df['storeid']

# 使用 CountVectorizer 進行 word count
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

# 處理 NaN 值，這裡使用中位數填充，你也可以選擇其他方式，如平均值
y.fillna(y.median(), inplace=True)

# 進行訓練集和測試集的劃分
X_train, X_test, y_train, y_test, store_ids_train, store_ids_test = train_test_split(X, y, store_ids, test_size=0.2, random_state=42)

# 初始化 Multinomial Naive Bayes 分類器
clf = MultinomialNB()

# 訓練模型
clf.fit(X_train, y_train)

# 進行預測
y_pred = clf.predict(X_test)

# 計算準確率
accuracy = accuracy_score(y_test, y_pred)

print(f"Accuracy: {accuracy}")

## 選擇一個店家（這裡以第一個店家為例）
selected_store_id = store_ids_test.iloc[0]

# 選取特定店家的評論
selected_store_comments = df[df['storeid'] == selected_store_id]

# 取得原本評論的所有欄位，包括 'text'、'storeid'、'effflag' 等
selected_store_comments_text = selected_store_comments['segmented']
selected_store_comments_storeid = selected_store_comments['storeid']
selected_store_comments_effflag = selected_store_comments['effflag']

# 使用訓練好的模型進行預測
selected_store_comments_vectorized = vectorizer.transform(selected_store_comments_text)
predictions = clf.predict(selected_store_comments_vectorized)

# 創建包含原本評論所有資訊和預測結果的 DataFrame
results = pd.DataFrame({
    'Comment': selected_store_comments_text,
    'StoreID': selected_store_comments_storeid,
    'EffFlag': selected_store_comments_effflag,
    'Prediction': predictions
})

# 匯出預測結果為 CSV 檔案，使用 mode='a' 附加到現有檔案，header=False 避免寫入標題
results.to_csv('Gappdj_finish.csv', mode='a', header=False, index=False, encoding='cp950')

