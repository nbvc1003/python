import numpy as np

a = np.array([2,4,6,8]).reshape(2,2)
b = np.array([2,2,2,2]).reshape(2,2)

print(a)
print(b)

print(a+b)
print(a-b)
print(a*b)
print(a/b)

# 행열의 곱셈
print(np.matmul(a,b))
