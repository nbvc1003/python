import pandas as pd
import numpy as np

fr = pd.DataFrame(np.arange(8).reshape(2,4),
                  index=['three', 'one'], columns=['d','a','b','c'])

print(fr)

print(fr.sort_index()) # index 기준 즉 행의 순서 정렬
print(fr.sort_index(axis=1)) # column 즉 열의 순서 정렬
# 숫서를 알수 있는 값들만 가능

print(fr.sort_index(ascending=False, axis=1)) # 내림차순 ( 큰수부터 ) default 오름차순 (작은수부터)

print(fr.sort_values(by='b')) #  b열 의 데이터 값 기준 오름차순
print(fr.sort_values(ascending=False,by='b')) # 내림차순