#查看空白欄位
import pandas as pd

# 載入 CSV 文件
file_path = 'Gappdj_segmented_no_with_total_eff.csv'  # 替換為你的檔案路徑
df = pd.read_csv(file_path, encoding='cp950')

# 檢查 'eff' 欄位是否有空白值
empty_eff_cells = df['eff'].isnull()

# 打印包含空白 'eff' 欄位的行
rows_with_empty_eff = df[empty_eff_cells]
print(rows_with_empty_eff)