from pandas import Series, DataFrame

items = {'code': [1,2,3,4,5,6],
'name': ['apple','watermelon','oriental melon', 'banana', 'lemon', 'mango'],
'manufacture': ['korea', 'korea', 'korea','philippines','korea', 'taiwan'],
'price':[1500, 15000,1000,500,1500,700]}

data = DataFrame(items, columns=['code','name','manufacture','price'])
print(data)
print(data['name'])
# print(data.ix[0]) # 없어질 예정 사용하지 않을것 loc or iloc 로 대체 필요

print('------------------------------------------------')
#
print(data.iloc[0])
print('------------------------------------------------')
#            열,   행       slice   열
print(data['name'][0], data[:1]['name'], data.loc[0,'name'])
