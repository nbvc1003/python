import pandas as pd
import numpy as np
from pandas import Series, DataFrame
stock1 = {'name': ['다음',"네이버", "넥슨", "NC"],
'2017-03-20': [84900, 818000, 1756,292000],
'2017-03-21': [86100, 871000, 1776,295000]}
stock2 = {'name': ['다음',"네이버", "넥슨","구글"],
'2017-04-20': [90800, 796000, 1695, 366500],
'2017-04-21': [90600, 806000, 1703, 358500]}
df1 = pd.DataFrame(stock1, columns=['name', '2017-03-20', '2017-03-21'])
df2 = pd.DataFrame(stock2, columns=['name', '2017-04-20', '2017-04-21'])

# 양쪽에 공통적인 column 이 존재 하는 내용만 결합
result = df1.merge(df2)
print(result)

# 양쪽에 name  column 이 존재 하는 내용만 결합
result2 = df1.merge(df2, on='name') # 위랑 같다.
print('=======================')
print(result2)

# 한쪽만 존재해도 결합
result3 = df1.merge(df2, on='name', how='outer')
print('=======================')
print(result3)