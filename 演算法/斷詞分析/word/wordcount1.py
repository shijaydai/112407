from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import glob

# 載入CSV文件
#file_path = 'Gappdj_segmented_no.csv'  # 替換為你的檔案路徑
file_path = 'runno.csv'  # 替換為你的檔案路徑
df_chunk_iter = pd.read_csv(file_path, encoding='cp950', chunksize=1000)  # 調整 chunksize 根據需求

# 初始化CountVectorizer，使用稀疏矩陣格式
vectorizer = CountVectorizer(min_df=1)  # 添加 min_df 參數，表示一個文件至少包含一個詞

result_dfs = []

# 逐批次處理資料
for i, df_chunk in enumerate(df_chunk_iter):
    # 處理 NaN
    df_chunk['segmented'] = df_chunk['segmented'].fillna('')

    # 將文本轉換為詞頻稀疏矩陣
    X_sparse = vectorizer.fit_transform(df_chunk['segmented'])

    # 將詞頻稀疏矩陣轉換為DataFrame
    word_count_df = pd.DataFrame.sparse.from_spmatrix(X_sparse, columns=vectorizer.get_feature_names_out())

    # 將詞頻DataFrame與原始資料合併
    result_df_chunk = pd.concat([df_chunk.reset_index(drop=True), word_count_df], axis=1)

    # 保存結果到新的CSV文件
    output_file_path = f'Gappdj_wordcount_chunk_{i + 1}.csv'
    result_df_chunk.to_csv(output_file_path, index=False, encoding='cp950')
    result_dfs.append(result_df_chunk)

# 合併所有結果
final_result_df = pd.concat(result_dfs, ignore_index=True)

# 保存最終結果到新的CSV文件
#inal_output_file_path = 'Gappdj_wordcount_final.csv'
final_output_file_path = 'final.csv'
final_result_df.to_csv(final_output_file_path, index=False, encoding='cp950')
