import pandas as pd
import numpy as np

# 인자의 합계를 리턴하는 함수
def func(x):
 return x.sum()

# 람다 방식
#f = lambda x: x.sum()

items = {'apple':{'count':10,'price':1500},
         'banana': {'count':5, 'price': 15000},
         'melon': { 'count':7,'price': 1000},
         'kiwi': {'count':20,'price': 500},
         'mango': {'count':30,'price': 1500},
         'orange': { 'count':4,'price': 700}}

data = pd.DataFrame(items)

data = data.T
print(data)
print("===============")

# 합계를 정리해서 보여준다 , 디폴트 열단위 합계..
print(data.apply(func))
print("===============")
# 행 단위 합계를 알려준다.
print(data.apply(func, axis=1))
