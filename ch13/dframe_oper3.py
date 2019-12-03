import pandas as pd
import numpy as np

np.random.seed(seed=123)
df = pd.DataFrame(np.random.randint(10, size=(4,8))) # (4,8) 사이즈의 0~10 랜덤 정수

print(df)

df['합계'] = df.sum(axis=1) # axis=1 행의합계
df.loc["계",:] = df.sum() # 열의 합계
print(df)


