import pandas as pd

# 성별이 index가 됨
df = pd.read_csv('tips.csv', index_col='sex')
print(df)
print('===========================================')
# df.groupby(len) # 인덱스 키값의 길이를 기준으로 분류한다. (male : 4자, female : 6자)
print(df.groupby(len).mean())


