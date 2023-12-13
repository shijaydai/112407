import pandas as pd

# 讀取 CSV 檔
data = pd.read_csv('store_effectiveness.csv', encoding='cp950')

# 將 0 變成 1，1 變成 0
data['effflag'] = data['is_positive'].replace({0: 1, 1: 0})

# 將修改後的資料匯出成 CSV 檔
data.to_csv('VADER1.csv', index=False)
