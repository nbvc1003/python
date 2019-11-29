# ar1 : 0~7 ar2 : 21 ~ 28
# br : ar1 을 ar2옆으로 붙여서 만들고
# br : 갯수, 평균, 분산, 표준편차, 최대, 최소 , 중앙


import numpy as np

ar1 = np.arange(0,7)
ar2 = np.arange(21,28)

br = np.hstack([ar1, ar2])
print(br)

print(len(br), np.mean(br), np.var(br), np.std(br), np.max(br),np.min(br), np.median(br))