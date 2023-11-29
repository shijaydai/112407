import pandas as pd
import glob

# 設定要從第 I 列開始加總
start_column_index = 9  # 這裡可以替換成你想要的起始列索引

# 取得所有檔案路徑
file_paths = glob.glob('Gappdj_wordcount_chunk_*.csv')

# 初始化結果列表
result_totals = []

# 逐個檔案進行加總
for file_path in file_paths:
    # 讀取檔案
    df = pd.read_csv(file_path, encoding='cp950')

    # 取得要加總的欄位
    columns_to_sum = df.columns[start_column_index:]

    # 計算橫向加總
    total = df[columns_to_sum].sum(axis=1)

    # 將加總結果新增到 DataFrame
    df['total'] = total

    # 保存結果到新的 CSV 文件
    output_file_path = file_path.replace('Gappdj_wordcount_chunk_', f'Gappdj_wordcount_total_{start_column_index}_')
    df.to_csv(output_file_path, index=False, encoding='cp950')

    # 將結果加入列表
    result_totals.append(df)

# 結束後，可以選擇合併所有橫向加總的 DataFrame
final_result_total = pd.concat(result_totals, ignore_index=True)

# 保存最終結果到新的 CSV 文件
final_output_file_path = 'Gappdj_wordcount_final_total.csv'
final_result_total.to_csv(final_output_file_path, index=False, encoding='cp950')
