import pandas as pd

items = pd.read_csv('tdata.csv', encoding='utf-8')
print(items)

# 통계적 설명
print(items.describe())

# 성적에 대한 설명
print(items['성적'].describe())

# value 값이 같은 항목의 갯수
print('빈도수 :',items['성적'].value_counts())