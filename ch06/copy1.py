import copy

a = [1,2,3]
x = [a, 100]

# 데이터를 복사하되 하위 원소의 데이터는 주소값으로 복사된다.
y = copy.copy(x) # 데이터를 복사한다.
# y = x.copy() # 위와 같다.
print(y)
x[1] = 200

print(x,y)

x[0][0] = 100
print(x, y)



