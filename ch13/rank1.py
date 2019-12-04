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
print(data.rank()) # 데이터의 순위를 출력 (작은순으로)
# 같을경우 평균 값을
print(data.rank(ascending=False)) # 큰순
print("===============")
print(data.rank(ascending=False)) # 동점일때 평균
print(data.rank(ascending=False, method='min')) # 동점일때 낮은 랭크값으로
print(data.rank(ascending=False, method='max')) # 동점일때 높은 랭크값으로
print(data.rank(ascending=False, method='first')) # 먼저나오는 값이 우선 랭크값으로
# print("===============")
