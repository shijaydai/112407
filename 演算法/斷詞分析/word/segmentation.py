import jieba.posseg as pseg
import pandas as pd

# 載入CSV文件
file_path = 'word.csv'  # 將 'your_file.csv' 替換為你的檔案路徑
df = pd.read_csv(file_path, encoding='cp950')

# 定義斷詞函數，包含詞性
def segment_text_with_pos(text):
    words = pseg.cut(text)
    segmented_text = []
    for word, pos in words:
        segmented_text.append(f'{word}({pos})')
    return ' '.join(segmented_text)

# 對DataFrame的某一列進行斷詞和顯示詞性
column_to_segment = 'comment'  # 將 'column_name' 替換為你想要斷詞的列名稱
df['segmented_text_with_pos'] = df[column_to_segment].apply(segment_text_with_pos)

# 保存結果到新的CSV文件
output_file_path = 'output_segmented_with_pos.csv'
df.to_csv(output_file_path, index=False, encoding='cp950')

