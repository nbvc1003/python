import pandas as pd

# 2019-12-04 기준으로 날짜를 5일간 생성
data_idx = pd.date_range('12/04/2019', periods=5, freq='D')
print(data_idx)

df1 = pd.DataFrame({'c1':[10,20,30,40,50]}, index=data_idx)
print(df1)

data_idx2 = pd.date_range('12/03/2019', periods=9, freq='D') # 2019/12/04 부터 일단위로 9일간

# bfill -> 숫서상 뒤쪽의 인덱스의 빈 데이터를 가까운곳의 데이터로 채운다.
df2 = df1.reindex(data_idx2, method='bfill')
print(df2)

# ffill -> 숫서상 앞쪽의 인덱스의 빈 데이터를 가까운곳의 데이터로 채운다.
df2 = df1.reindex(data_idx2, method='ffill')
print(df2)

