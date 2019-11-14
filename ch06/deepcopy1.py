
import copy

a = [1,2,3]
x = [a, 100]

# 각 원소 데이터의 하위 데이터의 값까지 전부 데이터로 복사한다.
y = copy.deepcopy(x) # 데이터를 복사한다.
# y = x.copy() # 위와 같다.
print(y)
x[1] = 200

print(x,y)

x[0][0] = 100
print(x, y)