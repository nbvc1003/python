from pandas import Series, DataFrame
import numpy as np

items = {'code': [1,2,3,4,5,6],
'name': ['apple','watermelon','oriental melon', 'banana', 'lemon', 'mango'],
'manufacture': ['korea', 'korea', 'korea','philippines','korea', 'taiwan'],
'price':[1500, 15000,1000,500,1500,700]}

data = DataFrame(items, columns=['code','name','manufacture','price'])

print(data)
print('-------------------------------------------------')
print(data.index)
data.index = np.arange(1, 7, 1)
print(data.index)
# data.price = [1500, 10000, 500,1200,300,5000]
# data.price = Series([3000,20000, 300, 1000], index=[1,2,3,4]) # 인덱스를 지정해서 넣어 준다.
#                index: 0     1    2     3
data.price = Series([3000,20000, 300, 1000]) # 인덱스 지정없을경우 0번부터 값이 들어간다. 0번은 컬럼 타이틀로 값을 넣을수 없다. 
print(data)