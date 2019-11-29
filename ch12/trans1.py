import numpy as np
ar = np.arange(10).reshape(2,5)

print(ar)

# a.T : 행과 열을 바꿔 주는 함수 ..
print(ar.T)
print(ar.transpose()) # 같은 기능

#0~19 (4,5) -> (5,4) 변경

br = np.arange(0,20).reshape(4,5)
print(br)
print(br.T)
print(br.transpose())
