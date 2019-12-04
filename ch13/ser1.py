import pandas as pd

s1 = pd.Series(['blue','purple','yellow'],
               index=[0,2,4]) # 인덱스는 숫서를 알수 있는 형식.
print(s1)

# 인덱스를 갱신 method = ffill, bfill  -> 이때 빈 인덱스일경우 데이터를 채우는 방법 지정
s2 = s1.reindex(range(6), method='ffill')
# ffill : forward fill 순서상 앞쪽데이터로 채운다.
# bfill : back fill 순서상 뒤쪽 데이터로 채운다.

