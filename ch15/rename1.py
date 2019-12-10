import pandas as pd
import numpy as np
from pandas import Series, DataFrame

stock = {
        '2017-03-20': [84900, 1756,292000],
        '2017-03-21': [86100, np.nan,295000]}

df = pd.DataFrame(stock, index=['다음','넥슨','NC'])

# rename, replace
# dictionary 를 인자로 사용하여 원하는 조건에 따라 값을 바꿔 준다.

print(df)
print('=============================================')
# 속성, 키 의 값을 바꿔준다.
df = df.rename(index={'다음':'daum','넥슨':'nexon'})
print(df)
print('=============================================')
# 값을 바꿔준다.
df = df.replace({np.nan:'-'})
print(df)