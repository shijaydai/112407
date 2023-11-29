import pandas as pd
import jieba

def segment_text(text):
    try:
        # 將 NaN 或其他非字符串值轉換為字符串
        text = str(text)
        words = jieba.cut(text)
        return " ".join(words)
    except Exception as e:
        print(f"Error processing text: {text}, Error: {e}")
        return ""

# 讀取 CSV 檔案
file_path = "Gappdj.csv"
df = pd.read_csv(file_path, encoding='cp950')

# 檢查並處理缺失值
df['comment'].fillna("", inplace=True)

# 指定要斷詞的欄位
column_to_segment = 'comment'

# 進行斷詞
df['segmented'] = df[column_to_segment].apply(segment_text)

# 將結果保存為新的 CSV 檔案
output_file_path = "Gappdjj_segmented_no.csv"
df.to_csv(output_file_path, index=False, encoding='cp950')
