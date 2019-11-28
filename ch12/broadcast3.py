import numpy as np

ar1 = np.array([1,2,3])
br1 = np.arange(20,32).reshape(4,3)
print(ar1)
print(br1)
print(ar1 + br1)
print(ar1 * br1)

ar2 = ar1.reshape(3,1)
br2 = np.arange(20,32).reshape(3,4)
print(ar2)
print(br2)

print(ar2 - br2)
print(ar2 % br2)
