import pandas as pd

# 讀取 Gappdj_wordcount_total_eff.csv
total_eff_df = pd.read_csv('total_eff.csv', encoding='cp950')

# 讀取 Gappdj_segmented_no.csv
segmented_no_df = pd.read_csv('Gappdj_segmented_no.csv', encoding='cp950')

# 將兩個 DataFrame 根據 'id' 合併
merged_df = pd.merge(segmented_no_df, total_eff_df[['id', 'total', 'eff']], on='id', how='left')

# 保存結果到新的 CSV 文件
output_file_path = 'segmented_total_eff.csv'
merged_df.to_csv(output_file_path, index=False, encoding='cp950')
