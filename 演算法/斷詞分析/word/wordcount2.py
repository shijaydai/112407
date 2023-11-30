import pandas as pd
import jieba
from collections import Counter

# 讀取 CSV 檔案
file_path = "GappWord.csv"
df = pd.read_csv(file_path, encoding='cp950')

# 檢查並處理缺失值
df['segmented_text'].fillna("", inplace=True)

# 取得文本資料
text_data = df['segmented_text'].tolist()

# 斷詞並統計詞頻
word_counts = Counter()
for text in text_data:
    # 將 NaN 或其他非字符串值轉換為字符串
    text = str(text)
    words = jieba.lcut(text)
    word_counts.update(words)

# 將詞頻映射為數字
word_to_index = {word: idx + 1 for idx, (word, _) in enumerate(word_counts.most_common())}

# 將每個文本轉換為數字序列
numeric_data = [[word_to_index[word] for word in jieba.lcut(str(text))] for text in text_data]

# 新增一列 'numeric_column' 到 DataFrame
df['numeric_column'] = numeric_data

# 將結果保存為新的 CSV 檔案
output_file_path = "GappWordCount.csv"
df.to_csv(output_file_path, index=False, encoding='cp950')


