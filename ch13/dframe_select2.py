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
# data = data.T # == transpose() 행열을 바꾼다.
# print(data)
print('-------------------------------------------')
print(data['1'])
print(data[['1','3']])
print(data[:1])
print(data[1:3])

data = data.T
print(data)
print(data[data['price'] > 1000])

# loc , iloc 에서 행은 slice 사용 , 열을 지정할때는 slice를 사용하지 않는다.

print(data.iloc[0])
print(data.loc[:'1','name'])
print(data.loc['1':'2',['name','price']]) # ['1' ~ '2' 행] ,  ['name', 'price' 열]
print(data.loc[:'3',['name','price']]) # 문자일때는 :'3' 3포함됨

print(data.loc[data.price > 1000, ['name', 'price']])









