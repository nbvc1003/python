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

# f1 평균
# 열별 평균, 합계
# f2 현재값 * 2
# 열별 값 2배

#f = lambda x: x.sum()

def func_mean(x):
    return x.mean()

def func_x2(x):
    return x*2

# 열, 행 별 평균을 보여주는 행열 출력
print(data.apply(func_mean))
print(data.apply(func_mean, axis=1))

# 각원소의 *2 값을 보여주는 결과 출력
print(data.apply(func_x2))
