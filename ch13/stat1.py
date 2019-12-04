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
print("===============")
# .describe() -> pandas 내장 함수 갯수, 평균, 표준편차, 최소최대 중위값 등등
print(data.describe()) # 데이터의 정보 설명  
