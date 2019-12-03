from pandas import DataFrame

item1 = {'1':{'price':1500}, '2':{'price':15000}, '3':{'price':1000}}
item2 = {'1':{'price':1500}, '2':{'price':15000}, '4':{'price':1000}}


data1 = DataFrame(item1)
data2 = DataFrame(item2)

# .T -> DataFrame 내부 함수
data1 = data1.T; data2 = data2.T

print(data1)
print(data2)

print(data1 + data2) # 값을 알수 없는경우 NaN
print(data1.add(data2, fill_value=0)) # NaN값을 0으로 채운다.

