import pandas as pd

df = pd.read_csv('dataset.csv')

df.info()  # Thông tin tổng quát về DataFrame
df.describe()  # Thống kê mô tả cho các cột số

df.drop_duplicates()  # Loại bỏ các dòng trùng lặp
# Lấy hai cột 'Summary' và 'Content'

df_selected = df[['Summary', 'Content']]
# Xóa các dòng có giá trị thiếu trong toàn bộ DataFrame
df_cleaned = df_selected.dropna()



df_cleaned.info()  # Thông tin tổng quát về DataFrame
df_cleaned.describe()  # Thống kê mô tả cho các cột số

df_cleaned.to_csv('datasetafter.csv', index=False, encoding='utf-8-sig')  # Lưu DataFrame thành file CSV



