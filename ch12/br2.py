import numpy as np

ar = np.arange(5).reshape(1,5)
br = np.arange(5).reshape(5,1)

print(ar)
print(br)
print(ar+br) # 자동으로 행열의 사이즈를 맞추어 계산을 한다.





