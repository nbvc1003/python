from pandas import Series, DataFrame
import pandas as pd
import numpy as np
stocks = {'2017-02-19':{'다음':50300,"네이버": 51100},
        "2017-02-22":{'다음':50300, '네이버': 50800},
        '2016-02-23':{'다음':50800,'네이버': 53000}}
data = DataFrame(stocks).T
print(data)
print(data.diff()) # 차분값 앞데이터를 현재 데이터값으로 뺐을때값
print("===============")
# (현위치 – 앞데이터)/앞데이터

# 증가율 (현재값 - 앞값)/앞값 ==> pct_change()
print(data.pct_change())
print("===============")
