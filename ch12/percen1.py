import numpy as np
from scipy.stats import describe
import matplotlib.pyplot as plt

# scipy : 과학연산을 위한 모듈을 포함한 라이브러리
# scipy.stats : 통계관련 모듈

x = np.array([18, 5, 10, 23, 19, -8, 10, 0, 0, 5, 2, 15, 8,
 2, 5, 4, 15, -1, 4, -7, -24, 7, 9, -6, 23, -13])

x.sort() # 원본데이터를 크기순으로 정렬해서 저장해준다.
print(x)
# 전체 값중에서 %에 해당하는 값을 보여준다.
print(np.percentile(x, 0)) # 최소값
print(np.percentile(x, 25)) # 25%
print(np.percentile(x, 50)) # 중앙값
print(np.percentile(x, 75)) # 75%
print(np.percentile(x, 100)) # 최대값

# 과학통계 함수를 이용한 종합적인 정보
print(describe(x))

# skewness : 기울어짐 -값이면 기울기가 양수
# kurtosis : 표족한정도

# plt.hist(x)
plt.plot(x)
plt.show()




