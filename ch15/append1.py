import pandas as pd
stock1 = {
     '2017-03-20': [84900, 818000, 1756],
     '2017-03-21': [86100, 871000, 1776]}
stock2 = {
     '2017-03-20': [90800, 796000, 1695],
     '2017-03-21': [90600, 806000, 1703]}

df1 = pd.DataFrame(stock1, columns=['2017-03-20','2017-03-21'],index=['다음','넥센','NC'])
df2 = pd.DataFrame(stock2, columns=['2017-03-20','2017-03-21'],index=['다음','네이버','넥센'])

print(df1+df2)
# 인덱스가 의미가 없다고 보고 아래에 붙이기
print(df1.append(df2))

# 중복된 데이터일경우 먼저것(df1) 사용
print(df1.combine_first(df2))
print('=================================================')
import numpy as np
print(df1.combine(df2, np.minimum))









