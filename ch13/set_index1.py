import pandas as pd
import numpy as np

a1 = np.arange(12).reshape(3,4)

print(a1)

df1 = pd.DataFrame(np.vstack([['a','b','c','d'], a1]).T,
                   columns=['C1','C2','C3','C4'])
print(df1)

# 원 인덱스를 없애고 'C1' 열을 인덱스로 사용한다.
df2 = df1.set_index('C1')
print(df2)

#C1 인덱스를 없애고 C2를 인덱스로
df3 = df2.set_index('C2')
print(df3)

# 현재 인덱스르 컬럼으로 바꾸고 새로운 인덱스를 생성 (defalut 형으로)
df4 = df3.reset_index()
print(df4)
#현재 인덱스 열을 삭제, 인덱스는 default형으로로 생성)
df5 = df3.reset_index(drop=True)
print(df5)