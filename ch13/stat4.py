from pandas import Series, DataFrame
import pandas as pd
import numpy as np
items = {'apple':{'count':10,'price':1500},
         'banana': {'count':5, 'price': 15000},
         'melon': { 'count':7,'price': 1000},
         'kiwi': {'count':20,'price': 500},
         'mango': {'count':30,'price': 1500},
         'orange': { 'count':4,'price': 700}}

data = DataFrame(items).T
print(data)
#차분, 증가율,
print(data.diff())
print(data.pct_change())
# NA 를 0으로
print(data.fillna(0))
# NA를 drop
print(data.dropna())
# 전부 Na를 drop
print(data.dropna(how='all'))
# 차부한 결과가 None이면 0으로
print(data.diff().fillna(0))


