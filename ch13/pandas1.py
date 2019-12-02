from pandas import Series
import numpy as np

# key + value 형식의 데이터
good = Series([4000, 3000, 3500, 2000],
              index=['apple','apple','orange','kiwi'])

print(good[good> 3000]) # value 값이 3000이상인 데이터만
print("---------------------------")
print(good+100) # value에 100더해서

print("---------------------------")

print(np.sum(good)) # 값을 전부 더한다.

print("---------------------------")

values = (4000, 3000, 3500, 2000)
keys = ['apple','apple','orange','kiwi']
dict1 = dict(zip(keys, values)) # 키가 중복될수 없다. 뒤쪽 값으로 덮어씌워진다.
print(dict1)

