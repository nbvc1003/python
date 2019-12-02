import numpy as np

ar = np.array([90, 40, 30, 78])

ar.sort() #
print(ar[0:int(0.5*len(ar))]) # index 0부터 절반(50%) 지점 까지 출력

print(ar[-int(0.5*len(ar)):]) # 절반지점부터 : 0 까지 역순으로 출력


