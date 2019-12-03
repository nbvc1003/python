from pandas import DataFrame

items = {'code': [1,2,3,4,5,6],
        'name': ['apple','watermelon','oriental melon', 'banana', 'lemon', 'mango'],
        'manufacture': ['korea', 'korea', 'korea','philippines','korea', 'taiwan'],
        'price':[1500, 15000,1000,500,1500,700]
         }

column = ['code','name','manufacture','price']

data = DataFrame(items, index=items['code'], columns=column)





# 15000
#
print(data)
# name 출력
print(data['name']) # Series
print(data[['name']]) # DataFrame

# name, price
print(data[['name','price']])

# 0행
print(data[:1])

# 1행 4행
print(data[1:4])

print(data[data['price'] == 15000])

# watermelon
print(data[1:2]['name']) # [행][열]


