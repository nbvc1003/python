import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(10, 22).reshape(3, 4),
    index=["a", "b", "c"],
    columns=["A", "B", "C", "D"])

print(df)


print(df.iloc[0])

print(df.iloc[0,1])
print(df.iloc[:2,2]) # 0/1행 2열
print(df.iloc[0,-2:]) # 0행 -2열부터 끝까지

print(df.iloc[1:3, 1:3]) # 1~2행, 1~2열
print(df.iloc[-1]) # 마지막행  출력
df.iloc[-1] = df.iloc[-1] * 2 # 마지막 행 값만 수정
print(df) # 충력

