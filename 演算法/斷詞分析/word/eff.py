import pandas as pd
import glob

# 設定要從第 I 列開始計算 total 和 eff
start_column_index = 9  # 這裡可以替換成你想要的起始列索引

# 取得所有檔案路徑
file_paths = glob.glob('Gappdj_wordcount_total_9_*.csv')


# 初始化結果列表
result_totals = []

# 逐個檔案進行計算
for i, file_path in enumerate(file_paths):
    # 讀取檔案
    df = pd.read_csv(file_path, encoding='cp950')

    # 檢查是否已經存在 'id' 列，如果不存在，新增
    if 'id' not in df.columns:
        df.insert(0, 'id', i + 1)

    # 取得要計算的欄位
    columns_to_sum = df.columns[start_column_index:]

    # 計算 total 列
    df['total'] = df[columns_to_sum].sum(axis=1)

    # 計算 eff 列
    df['eff'] = (df['total'] <= 6).astype(int)

    # 將結果加入列表
    result_totals.append(df[['id', 'total', 'eff']])

# 合併所有檔案
final_result_total = pd.concat(result_totals, ignore_index=True)

# 保存最終結果到新的 CSV 文件
final_output_file_path = 'Gappdj_wordcount_total_eff.csv'
#final_output_file_path = 'total_eff.csv'
final_result_total.to_csv(final_output_file_path, index=False, encoding='cp950')


