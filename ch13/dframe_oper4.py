import pandas as pd
import numpy as np

# 11~ 30 (4,5) -> DataFrame 
# 가로 세로 합계 추가

data = np.arange(11, 31).reshape(4,5)

data[0][0] = 2.5
print(data)
df = pd.DataFrame(data)
print(df)
df['합계'] = df.sum(axis=1) # axis = 0 이면 열단위로 합계를 산출
print(df)
df.loc['계',:] = df.sum() # axis = 0 이생략됨
print(df)
