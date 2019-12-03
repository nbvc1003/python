

from pandas import Series, DataFrame
import pandas as pd
import numpy as np
items = {'1':{'name':'apple', 'manufacture':'korea', 'price':1500},
        '2': {'name': 'watermelon', 'manufacture': 'korea', 'price': 15000},
        '3': {'name': 'oriental melon', 'manufacture': 'korea', 'price': 1000},
        '4': {'name': 'banana', 'manufacture': 'philippines', 'price': 500},
        '5': {'name': 'lemon', 'manufacture': 'korea', 'price': 1500},
        '6': {'name': 'mango', 'manufacture': 'korea', 'price': 700}}

data = DataFrame(items)
print(data)
data = data.T # == transpose() 행열을 바꾼다.
print(data)

# data1 = data.reindex(['1','2','3','4','5','7'], fill_value=0) # fill_value -> NaN값을 지정된값으로 채운다.
data1 = data.reindex(['1','2','3','4','5','7'], method='ffill') # method='ffill' -> 인덱스 값만 바꾸고 이전 데이터 값을 사용한다.
# index 6의 데이터는 삭제되고 인덱스 7은 NaN
print(data1)
