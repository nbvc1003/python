import numpy as np

ar = np.arange(1, 25).reshape(4,6)
print(ar)
print(ar+100)

new_ar = np.full_like(ar, 100) # 형열의 갯수를 ar과 같고 초기 값을 100으로 채우는 행열을 생성
print(new_ar)

print(ar+new_ar)

