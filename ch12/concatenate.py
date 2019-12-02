import numpy as np

ar1 = np.array([1,2,3,4])
br1 = np.array([5,6,7,8])
cr1 = np.concatenate((ar1, br1))  # R 의 cbind 와유사 (새로운 배열 생성)
print(np.concatenate((ar1, br1))) # 합침
print(cr1)

print(np.add(ar1, br1)) # +

ar2 = np.array([[1,2], [3,4]])
br2 = np.array([[5,6], [7,8]])

cr1 = np.concatenate((ar2,br2), axis=0) # 위아래 rbind 유사 (행방향으로  붙인다.)
cr2 = np.concatenate((ar2,br2), axis=1) # 좌우 cbind 와 유사 (열방향으로 붙인다. )
print(cr1)
print(cr2)


