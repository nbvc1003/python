from pandas import Series, DataFrame

item1 = {'1':{'price':1500}, '2':{'price':15000}, '3':{'price':1000}}
item2 = Series([300, 200,100], index =["1","2","4"])

data1 = DataFrame(item1)

print(data1 + item2)

# print(data1.add(item2, fill_value=0))  # DataFrame + Series 일때 fill_value 지원하지 않음
print(data1.add(item2))

data1 = data1.T
print(data1.add(item2, axis = 0))


