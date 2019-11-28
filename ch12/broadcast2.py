import numpy as np

ar = np.array([10,20,30])
br = np.arange(12).reshape((4,3)) # == (4,3)과 동일

print(br)
print(ar +br)

ar2 = ar.reshape(3,1)
print(ar2)
br2 = np.arange(10,22).reshape((3,4))

print(ar2 + br2)
