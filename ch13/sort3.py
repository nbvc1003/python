import pandas as pd

items = {'code': [1,2,3,4,5,6],
        'name': ['apple','watermelon','oriental melon', 'banana', 'lemon', 'mango'],
        'manufacture': ['korea', 'korea', 'korea','philippines','korea', 'taiwan'],
        'price':[1500, 15000,1000,500,1500,700]
         }

column = ['code','name','manufacture','price']

data = pd.DataFrame(items, index=items['code'], columns=column)

print(data)

# index 내림차순
print(data.sort_index())
# index 오름차순
print(data.sort_index(ascending=False))
# column 내림차순
print(data.sort_index(axis=1))

# 컬럼 오름차순
print(data.sort_index(ascending=False, axis=1))
# 가격 내림차순
print(data.sort_values(by= 'price'))
# 가격이 같으면 이름 오름차순
print(data.sort_values(ascending=[True,False], by=['price','name']))
