import numpy as np

a1 = np.ones((2,3))
print(a1)
a2 = np.zeros((2,2))
print(a2)

# 수평으로 붙인다.horizontal stack cbing와 유사 하다.
print(np.hstack([a1, a2]))

a3 = np.zeros((3,3))
print(a3)

# vstack vertical stack 수직으로 이어 붙임... rbind 와 유사..

print(a3)
a4 = np.vstack([a1, a3])
print(a4)
print(a1)

