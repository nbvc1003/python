
import pandas as pd
import numpy as np


df = pd.DataFrame(np.arange(10, 22).reshape(3, 4),
    index=["a", "b", "c"],
    columns=["A", "B", "C", "D"])

print(df)
print('----------------------------------------------------------')
# df[열] : 열의 데이터 조회

# a 행을 조회한다. 
print(df.loc['a'])
print(df.loc['b':'c'], type(df.loc['b':'c'])) # b~c행 조회

print(df.loc[['b','c']], type(df.loc[['b','c']]))

# (형, 열) 순으로 인자값 ([배열 or 조건 or ], [배열 or 조건 or]
print(df.loc['a', 'A'])
print(df.loc['a',:]) # a행의 모든열

print(df.loc[['a','b'],['B','D']]) # ab행 BD열
print(df.loc[df.A > 10, ['C', 'D']]) # 조건의 C D 값

print(df.loc['a':'c','A':'D'])
