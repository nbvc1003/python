from pandas import Series, DataFrame
import pandas as pd
import numpy as np
stocks = {
        '2017-02-19':{'다음':50300,"네이버": 51100, "넥슨":None, "NC":None},
        "2017-02-22":{'다음':50300, '네이버': 50800, "넥슨":35000, "NC":None},
        '2017-02-23':{'다음':50800,'네이버': 53000, "넥슨":37000, "NC":8000}}

data = DataFrame(stocks)
print(data)
print("===============")
data = data.T
print(data)
print("===============")
print(data.diff())
print("===============")
print(data.pct_change())
print("===============")

print("===============")
print("=.dropna()==============")
# 한개라도 NaN가 포함된 데이터는 삭제..
print(data.dropna())
print("==.fillna(0)=============")
# NaN값을 0 으로
print(data.fillna(0))
print("==(how='all')=============")
# 행의 모든 데이터가 NaN일경우에만 삭제
print(data.dropna(how='all')) # 모든 행이 NaN인 경우만 제외
print("===============")
# 차분을 계산하고 NaN데이터를 0으로 채운다.
print(data.diff().fillna(0))