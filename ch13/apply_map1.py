import pandas as pd

f1 = lambda x:x*2

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
print(data.applymap(f1)) # 각각의 데이터에 적용할때
print(data.apply(f1)) # 위와 동일
print(data['count'].map(f1)) # 하나의 컬럼 즉 Series 일경우 map() 을 사용한다.
print(data['price'].map(f1))