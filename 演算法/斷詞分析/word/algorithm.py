import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 載入CSV文件
file_path = 'Gappdj_wordcount_chunk_1.csv'  # 替換為你的檔案路徑
df = pd.read_csv(file_path, encoding='cp950')

# 假設 'target' 是目標變數，其他欄位是特徵
X = df.drop('target', axis=1)
y = df['target']

# 將資料分為訓練集和測試集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 初始化GradientBoostingClassifier
clf = GradientBoostingClassifier()

# 訓練模型
clf.fit(X_train, y_train)

# 預測測試集
y_pred = clf.predict(X_test)

# 評估模型性能
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

# 顯示評估結果
print(f'Accuracy: {accuracy}')
print('Confusion Matrix:')
print(conf_matrix)
print('Classification Report:')
print(classification_rep)
